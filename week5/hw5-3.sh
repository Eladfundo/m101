#/usr/bin sh
mongoimport -d m101 -c grades53 --drop < grades.json
mongo < hw5-3.txt
