#-*- encoding=utf-8 -*-

#将Flask框架导入
from flask import Flask

#创建一个应用类
app=Flask(__name__);

#以装饰器的方式设置url映射(支持多个映射)
@app.route("/index/")
@app.route("/")
def index():
	"""
		默认页面函数
		:return:页面内容
	"""
	return "hello world".capitalize()#首字母大写


@app.route("/profile/<uid>/")#<uid>表示以profile/之后的部分，可以直接作为参数使用
def profile(uid):
	return "profile:"+uid


@app.route("/profile/<int:uid>/")#<uid>表示以profile/之后的部分，可以直接作为参数使用
def get_age(uid):
	return "age:"+str(uid)

if __name__=="__main__":
	#启动应用
	app.run(debug=True)