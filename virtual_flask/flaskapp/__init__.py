from flask import Flask, make_response, Response

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
	print("before request!!")

@app.route('/res1')
def res1():
	custom_res = Response("Custom Response", 200, {'test': 'ttt'})
	return make_response(custom_res)

@app.route("/")
def helloworld():
	return "Hello Flask World!"


@app.route('/form', methods=['GET', 'POST'])
def parse_request():
	data = request.data

