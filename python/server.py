from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'incognitoModeDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/incognitoModeDB'

mongo = PyMongo(app)

# http://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value?noredirect=1&lq=1
def build_dict(seq, key):
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

@app.route('/getSessionData', methods=['GET'])
def getSessionData():
    idCollection = mongo.db.currID

    # finds and updates current id
    currID = idCollection.find_one_and_update({},{'$inc':{'id':1}})['id']

    questionArray = []

    qCollection = mongo.db.questions

    for q in qCollection.find():
        questionArray.append({'qid': q['qid'], 'qtext': q['qtext'], 'qtype': q['qtype'], 'qcount': q['qcount']})

    return jsonify({'id' : currID, 'questions' : questionArray})

@app.route('/submit', methods=['POST'])
def submit():
    req = request.get_json(force=True)

    uid = req['id']
    qid = req['qid']
    answer = req['answer']

    qCollection = mongo.db.questions
    aCollection = mongo.db.answers

    qCollection.find_one_and_update({'qid' : qid}, {'$inc': {'qcount': 1}})

    entry = aCollection.find_one({'id': uid})
    if entry:
        aCollection.update({'id': uid},{'$push': { 'answers' : {'qid': qid, 'answer': answer}}})
    else:
        aCollection.insert_one({'id': uid, 'answers': [ {'qid': qid, 'answer': answer}]})

    return jsonify({'result' : 'Success'})

@app.route('/finish', methods=['POST'])
def finish():
    req = request.get_json(force=True)

    uid = req['id']

    qCollection = mongo.db.questions
    aCollection = mongo.db.answers

    entry = aCollection.find_one({'id': uid})
    rand = entry

    if mongo.db.command('collStats','answers')['count'] != 1:
        rand = aCollection.aggregate([{'$sample':{ 'size':1}}]).next()

        while rand['id'] == uid:
            rand = aCollection.aggregate([{'$sample':{ 'size':1}}]).next()

    randID = rand['id']
    answersToPrint = []

    randAnswerMap = build_dict(rand['answers'], key='qid')

    for answer in entry['answers']:
        qid = answer['qid']

        if qid in randAnswerMap:
            answersToPrint.append(randAnswerMap[qid])

    qaList = []
    for answer in answersToPrint:
        question = qCollection.find_one({'qid': answer['qid']})

        qaPair = {
            'q': question['qtext'],
            'a': answer['answer']
        }

        qaList.append(qaPair)

    return jsonify({'result': { 'id': uid, 'randId': randID, 'randQA': qaList}})

if __name__ == '__main__':
    app.run(debug=True)
