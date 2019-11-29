import os
from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from abcd import *

app = Flask(__name__)
app.debug = True

cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(options={
	'databaseURL': 'https://fbtest-a36f5.firebaseio.com'
})
ref = db.reference('빕스')


@app.route("/readdb")
def readdb():
	빕스 = ref.get()
	print(ref.get())
	print()

	가맹점 = [빕스]
	가맹점명 = ['빕스']

	price=12000
	place='빕스'
	concard=['CJ ONE 신한카드', '하나 Yes OK Saver']
	print(allin(price, place, concard, 가맹점명, 가맹점))

	return 'OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)
