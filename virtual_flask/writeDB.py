import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import my_crawler

cred = credentials.Certificate("./fbtest-a36f5-firebase-adminsdk-g9u4b-2b258b2506.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
'''
doc_ref = db.collection(u'HomeAutomatic').document(u'RaspberryPi')
doc_ref.set({
	u'CPUTemp' : 100
})
'''


list_data = my_crawler.빕스

for lst in list_data:
	doc_ref = db.collection(u'data').document(lst[0])
	doc_ref.set({
		u'min' : lst[1],
		u'수식' : lst[2],
		u'real_cost' : lst[3],
		u'설명' : lst[4]
	})

