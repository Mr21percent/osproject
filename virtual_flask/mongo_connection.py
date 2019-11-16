HOSTNAME = "localhost"
PORT = 27017
import pymongo

client = pymongo.MongoClient(HOSTNAME, PORT)  #db접속주소
db = client.test  #데이터베이스명
collection = db.python  #db내의 컬렉션 선택

def seve(title, directorList, castList):
	collection.save({title": title, "director":directorList, "cast":castList})
