import os
from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from abcd import *
from tk_when_need_choice_card import *

app = Flask(__name__)
app.debug = True

cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(options={
	'databaseURL': 'https://fbtest-a36f5.firebaseio.com'
})
ref_vips = db.reference('빕스')
ref_user = db.reference('user_raspi')


@app.route("/readdb")
def readdb():
	user_raspi = ref_user.get()
	빕스 = ref_vips.get()
	print(user_raspi)

	가맹점 = [빕스]
	가맹점명 = ['vips']

	#price=12000
	#place='빕스'
	concard=['CJ ONE 신한카드', '하나 Yes OK Saver']
	price = int(user_raspi['price'])
	store = user_raspi['store']
	mci = allin(price, store, concard, 가맹점명, 가맹점)

	card_signal_data=[
			   ['CJ ONE 삼성카드', 'signal1'], 
			['CJ ONE 신한카드', 'signal2'], 
		   ['The CJ카드',' signal3'],
		   ['신한 Lady카드','signal4'],
		   ['삼성 SFC','signal5'],
		   ['삼성 T-Class Oil','signal6'],
		   ['삼성 Oil&Save Plus','signal7'],
		   ['삼성 S클래스카드', 'signal8'],
		   ['하나 Yes OK Saver','signal9'],
		   ['홈플러스 하나줄리엣카드','signal10'],
		   ['하나 줄리엣카드 & Yes 4u shopping','signal11'],
		   ['KB Star','signal12'],
		   ['이마트 KB카드', 'signal13']
	]

	last_tk(mci, price, card_signal_data)

	return 'OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)
