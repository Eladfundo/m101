
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades

def remove():

    #print "find, reporting for duty"

    try:
        itr = grades.find({'type':'homework'}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    student_id = None
    for doc in itr:
        if not student_id == doc['student_id']:
            grades.remove(doc)
        student_id = doc['student_id']

remove()

