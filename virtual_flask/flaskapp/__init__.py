from flask import Flask, render_template, request
from firebase import firebase

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

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return 'uploads 디렉토리 -> 파일 업로드 성공!'

@app.route('/index', methods=['GET'])
def index():
	testData = 'testData array'
	return render_template('')