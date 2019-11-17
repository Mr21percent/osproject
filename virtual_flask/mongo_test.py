HOSTNAME = "localhost"  #ip주소
PORT = 27017  #port번호
import pymongo

client = pymongo.MongoClient(HOSTNAME, PORT)  #client로 DB접속 주소를 정해줌
db = client.test  #db 객체 할당받기. DB_name = test
collection = db.python  #컬렉션 객체 할당받기. DB_collection_name = python

import datetime
post = {
"author" : "Mike",
"text" : "My first blog post!",
"tags" : ["mongodb", "python", "pymongo"],
"date": datetime.datetime.utcnow()
}

coll = db.collection
coll.insert(post)   #post_id = coll.insert(post)
post_id = coll.insert(post)

coll_list = db.collection_names()

'''
def save(title, directorList, castList):
	collection.save({"title": title, "director":directorList, "cast":castList})
'''
