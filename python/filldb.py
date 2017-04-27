from pymongo import MongoClient

def main():
    client = MongoClient('localhost:27017')
    db = client.incognitoModeDB

    db.currID.insert({"id":0})
    db.currID.find_one_and_update({},{'$inc':{'id':1}})['id']

    db.questions.insert({'qid': 2, 'qtext': 'jeff snyder is?', 'qtype': 'short', 'qcount': 0})

    db.answers.insert_one({'id': 4, 'answers': [ {'qid': 2, 'answer': "cool"}]})

if __name__ == '__main__':
    main()
