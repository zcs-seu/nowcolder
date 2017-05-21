#-*- encoding=utf-8 -*-

import random
from nowstgram import app,db
from nowstgram.models import User,Image,Comment
from flask_script import Manager
#导入sqlalchemy的或和与
from sqlalchemy import or_,and_

manager=Manager(app)


def get_image_url():
	return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'


@manager.command
def init_database():
	db.drop_all()#清空原有数据
	db.create_all()#重新新建类对应的表
	
	#测试添加
	
	#模拟添加一些数据
	for i in range(0,100):
		db.session.add(User('User'+str(i+1),'abc'+str(i+1)))
		for j in range(0,3):
			db.session.add(Image(get_image_url(),i+1))
			for k in range(0, 3):
				db.session.add(Comment('This is a comment'+str(k),1+3*i+j,i+1))
	db.session.commit()#数据库事务提交，不提交就相当于事务未发生
	
	#测试查询
	
	#全部查询
	#print 1,User.query.all()
	#按照主键查询
	#print 2,User.query.get(3)
	#实现按照某条件进行过滤
	#print 3,User.query.filter_by(id=5).all()
	#print 3,User.query.filter_by(id=5).first()
	#实现按照某一条件升序（降序）排列，向后偏移一个只取其中2个
	#print 4, User.query.order_by(User.id).offset(1).limit(2).all()
	#print 4, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
	#过滤查找某属性值以'0'结尾（开头）
	#print 5, User.query.filter(User.username.endswith('0')).all()
	#print 5, User.query.filter(User.username.startswith('1')).all()
	#使用或和与条件
	#print 6, User.query.filter(or_(User.username.endswith('99'),\
	#                               User.username.endswith('98'))).all()
	#print 6, User.query.filter(and_(User.id>89, \
	#                               User.id<91)).all()
	#分页查询
	#print 7, User.query.paginate(page=1,per_page=3).items
	#print 7, User.query.paginate(page=2, per_page=3).items
	#分页+逆序
	#print 8, User.query.order_by(User.id.desc()).paginate(page=2, per_page=3).items
	#打印正向外部关联的对象（1对多）
	#user=User.query.get(1)
	#print 9,user.images
	#打印反向外部关联的对象（多对1）
	#image=Image.query.get(1)
	#print 10,image.comments
	
	#测试更新
	
	#操作属性值更新
	'''
	for i in range(50,100,2):
		user=User.query.get(i)
		user.username='[New]'+user.username
	db.session.commit()
	print 11,User.query.get(52)
	'''
	#使用upadate更新
	'''
	User.query.filter_by(id=52).update({'username':'[New2]'})
	db.session.commit()
	print 12,User.query.get(52)
	'''
	
	#测试删除
	'''
	for i in range(50,100,1):
		#(1)
		#comment=Comment.query.get(i)
		#db.session.delete(comment)
		#(2)
		Comment.query.filter_by(id=i).delete()
	db.session.commit()
	print 13, Comment.query.get(51)
	'''

if __name__=='__main__':
	manager.run()