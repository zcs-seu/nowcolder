#-*- encoding=utf-8 -*-

#将Flask框架导入
from flask import Flask
#导入模板类
from flask import render_template
#导入request
from flask import request
#导入response
from flask import make_response
#导入redirect
from flask import redirect
#导入flash,get_flashed_messages
from flask import flash,get_flashed_messages
#导入日志处理所需包
import logging
from logging.handlers import RotatingFileHandler


#创建一个应用类
app=Flask(__name__);
#设置单行模板语句解析以#开头
app.jinja_env.line_statement_prefix="#"
#设置secret_key，否则sessionID将无法产生，正常情况下应该设置一个随机的无序值，
#作为页面的唯一代表
app.secret_key='nowcoder'

#以装饰器的方式设置url映射(支持多个映射)
@app.route("/index/")
@app.route("/")
def index():
	"""
		默认页面函数
		:return:页面内容
	"""
	res=''
	#取得带有类别信息的Flash_Message
	for msg,category in get_flashed_messages(with_categories=True):
		res+=category+msg+'<br>'
	res+='hello'
	return res#首字母大写


@app.route("/profile/<uid>/")#<uid>表示以profile/之后的部分，可以直接作为参数使用
def profile(uid):
	return "profile:"+uid


@app.route("/age/<int:age>/")#直接指定参数的类型
def get_age(uid):
	return "age:"+str(age)


@app.route("/name/<name>/",methods=['get','post'])#直接指定参数的类型、请求类型
def get_name(uid):
	return "name:"+str(name)


@app.route("/sex/<int:sex>/")#直接指定参数的类型、html模板、jinja语法
def get_sex(sex):
	colors=('red','green','yellow')
	dict={'1':'zcs','2':'gj'}
	return render_template('profile.html',sex=sex,colors=colors,dict=dict)


@app.route("/request")#直接指定参数的类型
def request_demo():
	res=request.args.get('key','default_key')+'<br>'
	res+=request.url+"<br>"+request.path
	response=make_response(res)
	response.set_cookie('zcs','gj')
	response.status='404'
	response.headers['love']='wxw'
	return response


@app.route("/newpath")#重定向后的函数
def new_path():
	res=request.args.get('key','default_key')+'<br>'
	res+=request.url+"<br>"+request.path
	response=make_response(res)
	response.set_cookie('zcs','gj')
	response.headers['love']='wxw'
	return response


@app.route("/redirect/<int:code>/")#直接重定向，code指定重定向类型
def redirect_demo(code):
	return redirect('/newpath',code=code)


@app.errorhandler(404)#设置统一的404异常处理机制
def page_not_found(error):
	print error
	return render_template('/not_found.html',url=request.url)


@app.route("/admin")#检查管理者权限
def admin():
	key=request.args.get('key')
	if key=='admin':
		return "hello admin"
	else:
		raise Exception()


@app.route('/login')
def login():
	log('error','登陆成功！')
	flash('登陆成功','info')#'info'为flash message的级别
	return redirect('/')


#设置log的公共入口
def log(level,msg):
	dict={'warn':logging.WARN,'info':logging.INFO,'error':logging.ERROR}
	if dict.has_key(level):
		app.logger.log(dict[level],msg)
	return 'logged:'+msg


#设置logger
def set_logger():
	
	info_file_handler=RotatingFileHandler('/log/flask-python/info.txt')
	info_file_handler.setLevel(logging.INFO)
	app.logger.addHandler(info_file_handler)
	
	warn_file_handler = RotatingFileHandler('/log/flask-python/warn.txt');
	warn_file_handler.setLevel(logging.WARN)
	app.logger.addHandler(warn_file_handler)
	
	error_file_handler = RotatingFileHandler('/log/flask-python/error.txt');
	error_file_handler.setLevel(logging.ERROR)
	app.logger.addHandler(error_file_handler)

if __name__=="__main__":
	#设置logger
	set_logger()
	#启动应用
	app.run(debug=True)