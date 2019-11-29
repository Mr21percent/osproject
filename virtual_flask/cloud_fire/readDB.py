import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./fbtest-a36f5-firebase-adminsdk-g9u4b-2b258b2506.json")
firebase_admin.initialize_app(cred,{
	'databaseURL' : 'https://fbtest.firebaseio.com/'
})


ref = db.reference()

print(ref.get())
