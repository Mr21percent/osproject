from flask import Flask, request, jsonify
#from firebase import firebase

app = Flask(__name__)
app.debug = True

@app.route("/")
def helloworld():
	return "Hello Flask World!"

'''
@app.before_request
def before_request():
	print("before request!!")
'''

@app.route('/index', methods=['GET'])
def index():
	testData = 'testData array'
	return render_template('')


@app.route('/test'
