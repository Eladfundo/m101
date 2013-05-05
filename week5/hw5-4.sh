#/usr/bin sh
mongoimport -d m101 -c zips --drop < zips.json
mongo < hw5-4.txt
