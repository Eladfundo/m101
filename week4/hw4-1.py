db.products.find({'brand':"GE"}).explain()
db.products.find({'brand':"GE"}).sort({price:1}).explain()
db.products.find({$and:[{price:{$gt:30}},{price:{$lt:50}}]}).sort({brand:1}).explain()
db.products.find({brand:'GE'}).sort({category:1, brand:-1}).explain()
