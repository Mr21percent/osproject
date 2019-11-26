from flask import Flask, request, jsonify
from my_crawler import *
from def_cardlist_with_sort import *


app = Flask(__name__)
app.debug = True

@app.route("/")
def helloworld():
	return "Hello Flask World!"

'''
@app.before_request
def before_request():
	print("before request!!")

@app.route('/index', methods=['GET'])
def index():
	testData = 'testData array'
	return render_template('')
'''

@app.route('/test')
def test():

	a=['우리체크', 0 ,'x*0.8',0,'20프로 할인']
	b=['우리신용', 10000 ,'x-3000.0',0,'결제 건당 3000원 할인']
	c=['CU·배달의민족 삼성카드 taptap', 1500, 'x-(x//1500)*200',0,'1500원 당 200원 할인']
	소지카드=['우리체크','CU·배달의민족 삼성카드 taptap']
	편의점=[a,b,c]
	스팅=[a,b,c]
	주유소=[a,b,c]
	가맹점명=["편의점", "주유소", "스팅", "빕스"]
	가맹점=[편의점, 주유소, 스팅, 빕스]

	imin="빕스"
	ls=card_sort(where(imin, 가맹점명, 가맹점),  800000)

	for i in range(len(ls)):
		print(ls[i][0],'\t',ls[i][3])
	print(ls[0][4])


	return jsonify(hello='world')

