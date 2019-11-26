import os
from flask import Flask, request, jsonify
import a
app = Flask(__name__)

a = 0

@app.route('/')
def Keyboard():
	a.printf()
#	print(b)
    return 'hi'

'''
@app.route('/test')
def test():
    global a
    a+=1
    return str(a)
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)
