#-*- encoding=utf-8 -*-
"""
	利用python装饰器（类似于java中的注解）实现在函数首尾添加函数功能，此时装饰器带有
	参数；
		如对输入进行预处理、验证;
		对输出结果进行修正等；
"""
def wrapper(level):
	"""
			定义了一个装饰器函数(带参数)
			:param func:
			:return:inner
		"""
	def inner(func):
		def new_func(*args,**kvargs):
			"""
			:param args: *表示无名参数
			:param kvargs: **表示有名参数
			:return:
			"""
			print "before call hello()",func.__name__
			print "args:",args,"kvargs:",kvargs
			func(name,age)
			print "level:",level
			print "after call hello()", func.__name__
		return new_func
	return inner


@wrapper(level="INFO")
def hello(name,age):
	"""
		定义了一个功能函数实例，输出“hello world！”
	"""
	print "hello world!",name,age


if __name__=="__main__":
	name="张成帅"
	age=23
	# 相当于wrapper(hello(name,age=age))
	hello(name,age=age) #其中name为无名参数，age为有名参数