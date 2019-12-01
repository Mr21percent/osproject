
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://fbtest-a36f5.firebaseio.com'
})

ref_user = db.reference('user_raspi') #db 위치 지정
ref_vips = db.reference('빕스')

user_raspi = ref_user.get()
빕스 = ref_vips.get()

print(user_raspi)
'''
price = int(user_raspi['price'])
store = user_raspi['store']
print("빕스 = ", 빕스)
print()
print('price = ', price)
print(type(price))
print('store = ', store)
print(type(store))
'''
