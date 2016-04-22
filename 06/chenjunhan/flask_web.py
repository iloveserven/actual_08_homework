#!/usr/bin/env python
# coding=utf-8
from flask import Flask,render_template,request,redirect,session
import util

util.update_data()
print util.file_date
app = Flask(__name__)
app.secret_key='nsifndsifionfonwien-1341NIUSNi'

@app.route('/login')
def login():
	if 'user' in session:
		return redirect('/')
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/login')

@app.route('/loginaction',methods=['post'])
def loginaction():
	user = request.form.get('user')
	passwd = request.form.get('passwd')
	if user=='admin' and passwd=='admin':
		session['user'] = 'admin'
	return redirect('/')

@app.route('/')
def index():
	if 'user' not in session:
		return redirect('/login')
	return render_template('data.html',userlist=util.file_date.items())

@app.route('/adduser',methods=['post'])
def adduser():
	print request.args
	user = request.form.get('user')
	password = request.form.get('password')

	if user in util.file_date:
		return 'user alreaday exists'
	else:
		util.file_date[user] = password
		util.update_data()
		return redirect('/')

@app.route('/deluser')
def deluser():
	print request.args
	user = request.args.get('user')
	if user in util.file_date:
		util.file_date.pop(user)
		print util.file_date
		util.update_data()
	return redirect('/')

if __name__=='__main__':
	app.run(host='0.0.0.0',port=9093,debug=True)

