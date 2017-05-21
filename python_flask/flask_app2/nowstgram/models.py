#-*- encoding=utf-8 -*-

import random
from nowstgram import db
from datetime import datetime

class User(db.Model):
	#用户类
	#__name__='xuser'#显式设置表名
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(32))
	#头像地址
	headurl = db.Column(db.String(256))
	#头像图片关联的表,并同时根据backref设置反向关联
	images=db.relationship('Image',backref='user',lazy='dynamic')
	
	#类的初始化函数
	def __init__(self,username,password):
		self.username = username;
		self.password = password;
		self.headurl = 'http://images.nowcoder.com/head/'+\
		               str(random.randint(0,1000))+'m.png'
	
	#该函数返回类对象的可打印字符串，类似于Java中的toString
	def __repr__(self):
		return '<User %d %s>' % (self.id,self.username)

class Image(db.Model):
	#与用户相关联的图片类
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
	url=db.Column(db.String(512))
	create_date=db.Column(db.DateTime)
	comments=db.relationship('Comment')
	
	def __init__(self,url,user_id):
		self.url=url
		self.user_id=user_id
		self.create_date=datetime.now()
	
	# 该函数返回类对象的可打印字符串，类似于Java中的toString
	def __repr__(self):
		return '<Image %d %s>' % (self.id, self.url)


class Comment(db.Model):
	# 评论类
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	content = db.Column(db.String(1024))
	image_id=db.Column(db.Integer,db.ForeignKey('image.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	status=db.Column(db.Integer,default=0)#0正常，1被删除，因为所有用户内容都应该保存作为证据
	user = db.relationship('User')
	
	def __init__(self,content,image_id,user_id):
		self.content = content
		self.image_id = image_id
		self.user_id = user_id
	
	# 该函数返回类对象的可打印字符串，类似于Java中的toString
	def __repr__(self):
		return '<Comment %d %s>' % (self.id, self.content)