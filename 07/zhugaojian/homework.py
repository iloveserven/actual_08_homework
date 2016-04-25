#!/bin/env python
# coding=utf-8

from flask import Flask,session,redirect,render_template,request
import mysqldb as db
import user
import access_log as a_log
import time

app = Flask(__name__)
app.secret_key='asdfqwew987aakfa98&*^(asfqwer'

@app.route('/')
def index():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	username = session['user']
	userlist = user.userlist()
	accesslist = a_log.access_log_list()
	return render_template('index.html',userlist=userlist,accesslist=accesslist,username=username,is_admin=is_admin)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/loginaction',methods=['post'])
def loginaction():
	is_admin = 0
	is_exist_user = 0
	username = request.form.get('username')
	password = request.form.get('password')
	sql = "select password from user where name='%s' and password='%s'"%(username,password)
	res = db.select_one(sql)
	if res['password'] == password:
		is_exist_user = 1
		session['user'] = username
	if username == 'admin' and password == 'admin':
		is_admin = 1
	session['is_admin'] = is_admin
	if is_exist_user:
		return redirect('/')
	else:
		return redirect('/login')


@app.route('/logout')
def logout():
	session.pop('user')
	session.pop('is_admin')
	return redirect('/login')

# sql = 'select * from user'
# print time.ctime()
# count = db.countselect(sql)
# print count
# res = db.select_all(sql)
# db.execute('insert into user(name,password) values("asas","asas")')
# db.close()
# print res
# print time.ctime()

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)