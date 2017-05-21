#-*- encoding=utf-8 -*-
from flask_script import Manager
from flask_app1 import app

manager=Manager(app)

@manager.option('-n','--name')
def hello(name):
	print "hello,",name


@manager.command
def initialize_database():
	'初始化数据库'#给出该函数的说明当使用python manager.py --help时可以使用
	print 'initialize the database'

if __name__=='__main__':
	#查看可以进行哪些操作
	manager.run()