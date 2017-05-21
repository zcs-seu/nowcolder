#-*- encoding=utf-8 -*-

from nowstgram import app
from flask import render_template

from models import User,Image,Comment

#首页
@app.route("/")
def index():
	images=Image.query.order_by('id').limit(10).all()
	return render_template('index.html',images=images)


#图片页
@app.route("/image/<int:image_id>")
def image(image_id):
	image=Image.query.get(image_id)
	if image==None:
		return redirect("/")
	return render_template('pageDetail.html',image=image)


#详情页
@app.route("/profile/<int:user_id>")
def profile(user_id):
	user=User.query.get(user_id)
	if user==None:
		return redirect('/')
	return render_template('profile.html',user=user)