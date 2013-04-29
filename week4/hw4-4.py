
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.m101
profile = db.profile

def find():

    query = {'ns':'school2.students'}
    selector = {'millis':1}

    try:
        cursor = profile.find(query,selector).sort('millis',pymongo.DESCENDING).limit(5)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break
find()
