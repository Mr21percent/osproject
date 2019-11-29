
import firebase_admin
from flask import *
from firebase_admin import db
import pyrebase

config = {
  apiKey: "AIzaSyAUNExg-kxrb8zwe9froWVAAWIUc6TL59s",
  authDomain: "fbtest-a36f5.firebaseapp.com",
  databaseURL: "https://fbtest-a36f5.firebaseio.com",
  projectId: "fbtest-a36f5",
  storageBucket: "fbtest-a36f5.appspot.com",
  messagingSenderId: "104090635814",
  appId: "1:104090635814:web:b725b0e558a149003aa0e7",
  measurementId: "G-M3BGE5CF0Y"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database().ref().on()

app = Flask(__name__)
app.debug = True
'''
firebase_admin.initialize_app(options={
	'databaseURL': 'https://fbtest-a36f5.firebaseio.com'
})
ref = db.reference('반원')
'''
@app.route("/")
def helloworld():
	return "Hello Flask World!"

@app.route("/readdb")
def readdb():
	a = db.child('반원').get().val().values()
	return a


