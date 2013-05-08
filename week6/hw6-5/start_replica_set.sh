killall mongod
# remove the directories
rm -rf /data/db/rs1 /data/db/rs2 /data/db/rs3
# create them
mkdir -p /data/db/rs1 /data/db/rs2 /data/db/rs3
mongod --replSet m101 --logpath "1.log" --dbpath /data/db/rs1 --port 27017 --smallfiles --oplogSize 200 --fork
mongod --replSet m101 --logpath "2.log" --dbpath /data/db/rs2 --port 27018 --smallfiles --oplogSize 200 --fork
mongod --replSet m101 --logpath "3.log" --dbpath /data/db/rs3 --port 27019 --smallfiles --oplogSize 200 --fork
