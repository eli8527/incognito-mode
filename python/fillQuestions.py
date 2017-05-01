from pymongo import MongoClient
import csv

def main():
    client = MongoClient('localhost:27017')
    db = client.incognitoModeDB

    # Reset all DBs
    db.currID.drop()
    db.questions.drop()
    db.answers.drop()

    # Set currID
    db.currID.insert({"id":0})
    # db.currID.find_one_and_update({},{'$inc':{'id':1}})['id']

    # Populate questions
    with open('questions.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            qid = int(row[0])
            qtext = row[1]
            qtype = row[2]

            db.questions.insert({'qid': qid, 'qtext': qtext, 'qtype': qtype, 'qcount': 0})

    db.create_collection('answers')
    # db.answers.insert_one({'id': 4, 'answers': [ {'qid': 2, 'answer': "cool"}]})
if __name__ == '__main__':
    main()
