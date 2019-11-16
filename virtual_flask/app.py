from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# ...

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #사용할 데이터베이스의 위치
app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False  #추가적 메모리를 필요로 하므로 꺼둠

db = SQLAlchemy(app)  #객체 생성

# ...

class User(db.Model):
	__table_name__ = 'user'

	username = db.Column(db.String(100), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)

	def __repr(self):
		return f"<User('{self.id}', '{self.username}', '{self.email}')>"
