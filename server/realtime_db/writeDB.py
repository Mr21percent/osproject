
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def read_txt(fname):
	vips = []
	openfile = open(fname,'r')

	rstr = openfile.readlines()
	for i in range(len(rstr)):
		rstr[i] = rstr[i].strip().split(',')
		if rstr[i] != ['']:
			print(rstr[i])
			vips.append(rstr[i])
	return vips


vips = read_txt('vips.txt')

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://fbtest-a36f5.firebaseio.com'
})

ref = db.reference() #db 위치 지정
ref.update({'빕스' : vips}) #해당 변수가 없으면 생성한다.

