
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students

def update():

    #print "find, reporting for duty"

    try:
        itr = students.find().sort('_id',pymongo.ASCENDING)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    student_id = None
    for doc in itr:
        scores = doc['scores']
        new_scores = []
        highest_hw = {'type':'homework', 'score': 0}
        for _doc in scores:
            if _doc['type'] == 'homework':
                if _doc['score'] > highest_hw['score']:
                    highest_hw = _doc
            else:
                new_scores.append(_doc)
        new_scores.append(highest_hw)
        students.update({'_id':doc['_id'] }, { '$set': { 'scores' : new_scores } });
update()

