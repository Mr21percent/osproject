HOSTNAME = "localhost"  #ip주소
PORT = 27017  #port번호
import pymongo

client = pymongo.MongoClient(HOSTNAME, PORT)  #클래스 객체 할당
db = client.test  #데이터베이스명. db_name = test
collection = db.python  #db내의 컬렉션 선택. collection_name = python

def save(title, directorList, castList):
	collection.save({"title": title, "director":directorList, "cast":castList})
