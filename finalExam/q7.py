import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.photosharing
albums = db.albums
images = db.images

print "ensure Indexes"
try:
    albums.create_index([("images", pymongo.ASCENDING)])
except:
    print "Unexpected error:", sys.exc_info()[0]
print albums.index_information()

try:
    images.create_index([("tags", pymongo.ASCENDING)])
except:
    print "Unexpected error:", sys.exc_info()[0]
print images.index_information()


print "As as a sanity check, there are 40,455 images that are tagged 'kittens' before query"
try:
    counter1 = db.images.find({"tags": "kittens"})
except:
    print "Unexpected error:", sys.exc_info()[0]
print counter1.count()

# all images

try:
    cursor = images.find(None, {"_id": 1})
except:
    print "Unexpected error:", sys.exc_info()[0]

for doc in cursor:
    img_id = doc["_id"]
    try:
        cursor2 = albums.find({"images": img_id})
    except:
        print "Unexpected error:", sys.exc_info()[0]

    ids = []
    if cursor2.count() == 0:
        # try:
        #     cursor2 = images.remove({"_id" : img_id})
        # except:
        #     print "Unexpected error:", sys.exc_info()[0]
        ids.append(img_id)

    try:
        remove = images.remove({"_id": {"$in": ids}})
    except:
        print "Unexpected error:", sys.exc_info()[0]


print "there should be 40,438 documents in the images collection."
count2 = db.images.find()
print count2.count()

print "Answer"
try:
    counter3 = db.images.find({"tags": "kittens"})
except:
    print "Unexpected error:", sys.exc_info()[0]
print counter3.count()
