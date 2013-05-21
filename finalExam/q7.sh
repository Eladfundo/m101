#/usr/bin sh
mongoimport -d photosharing -c albums --drop < albums.json
mongoimport -d photosharing -c images --drop < images.json
python q7.py
