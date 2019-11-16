HOSTNAME = "localhost"
PORT = 27017
import pymongo

client = pymongo.MongoClient(HOSTNAME, PORT)
	db = client.test
	collection = db.python

	def seve(title, directorList, castList):
		collection.save({title": title, "director":directorList, "cast":castList})
