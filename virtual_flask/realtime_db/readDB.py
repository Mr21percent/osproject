# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://fbtest-a36f5.firebaseio.com'
})

ref = db.reference('반원')
print(ref.get())
