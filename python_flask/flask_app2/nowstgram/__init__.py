#-*- encoding=utf-8 -*-

#加载Flask
from flask import Flask
#导入SqlAlchemy
from flask_sqlalchemy import SQLAlchemy

#创建app
app=Flask(__name__)

#配置app— —导入配置文件
app.config.from_pyfile('app.conf')

#为应用app添加循环控制,不加的话无法使用break、continue
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

#创建SQLAlchemy对象
db=SQLAlchemy(app)

from nowstgram import models,views