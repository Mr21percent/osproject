from flask import Flask
app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return 'Hello World!'

@app.route('/profile/<username>')
def hello_world(username):
    return 'profile: ' + username

host_addr = "0.0.0.0"
port_num = "8080"

if __name__=='__main__':
	with app.test_request_context():
		print(url_for('hello'))
		print(url_for('get_profile', username='flash'))
	# app.run(host=host_addr, port=port_num)
