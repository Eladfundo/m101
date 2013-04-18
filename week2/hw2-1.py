
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades

def find():
    query = {'type':'exam','score':{'$gte':65}}
    selector = {'student_id':1,'score':1}

    try:
        cursor = grades.find(query,selector).sort('score',pymongo.ASCENDING).limit(10)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break

find()
