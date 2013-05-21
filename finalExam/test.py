import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.photosharing
albums = db.albums
images = db.images

try:
    cursor = images.find(None, {"_id": 1})
except:
    print "Unexpected error:", sys.exc_info()[0]

try:
    cursor2 = albums.find(cursor, {"_id": 1})
except:
    print "Unexpected error:", sys.exc_info()[0]

sanity = 0
for doc in cursor2:
    print doc
    sanity += 1
    if (sanity > 10):
        break
