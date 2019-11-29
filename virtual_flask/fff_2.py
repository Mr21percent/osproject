'''
import requests
from requests.packages import urllib3
print(urllib3.__version__)
'''
import os
from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#import auth
'''
import pyrebase
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

db = firebase.database()
'''
# ...
app = Flask(__name__)
app.debug = True

cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(options={
	'databaseURL': 'https://fbtest-a36f5.firebaseio.com'
})
ref = db.reference('빕스')
'''
# uid
decoded_token = auth.verify_id_token(id_token)
uid = decoded_token['uid']
'''

def helloworld():
	return "Hello Flask World!"

@app.route("/readdb")
def readdb():
	'''
	userId = firebase.auth().currentUser.uid
	a = db.child("반원").get(token=user['idToken'])
	print(a)

	firebase = firebase.FirebaseApplication('https://fbtest-a36f5.firebaseio.com', None)
	print(firebase.get())

	hero = ref.child("vips").get()
	print(hero)
	'''
	print(ref.get())
	return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)
