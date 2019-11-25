import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'HomeAutomatic').document(u'RaspberryPi')
doc_ref.set({
	u'CPUTemp' : 100
})
