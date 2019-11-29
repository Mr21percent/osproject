'''
import requests
from requests.packages import urllib3
print(urllib3.__version__)
'''
#import auth
#import FirebaseAuth

import os
from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#import pyrebase
'''
config = {
  'apiKey': "AIzaSyAUNExg-kxrb8zwe9froWVAAWIUc6TL59s",
  'authDomain': "fbtest-a36f5.firebaseapp.com",
  'databaseURL': "https://fbtest-a36f5.firebaseio.com",
  'projectId': "fbtest-a36f5",
  'storageBucket': "fbtest-a36f5.appspot.com",
  'messagingSenderId': "104090635814",
  'appId': "1:104090635814:web:b725b0e558a149003aa0e7",
  'measurementId': "G-M3BGE5CF0Y"
}

firebase = pyrebase.initialize_app(config)

#auth = firebase.auth()
#user = auth.sign_in_with_email_and_password("maychoi410@gmail.com", "d0nothing-")
db = firebase.database()
'''
app = Flask(__name__)
app.debug = True

cred = credentials.Certificate('mykey.json')
'''
firebase_admin.initialize_app(options={
	'databaseURL': 'https://fbtest-a36f5.firebaseio.com'
})
'''
firebase_admin.initialize_app(cred)

@app.route("/")
def helloworld():
	return "Hello Flask World!"

@app.route("/readdb")
def readdb():
	ref = db.reference("반원")
	print(ref.get())
#	a = db.child("반원").get()
#	return a

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)
