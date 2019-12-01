import os
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hi():
	return 'hi'

@app.route('/test')
def test():
	'''
    global a
    a+=1
    return str(a)
	'''
	return 'test'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
