#!/usr/bin/python
#!coding:utf-8
from flask import Flask,render_template,request,redirect,session
app=Flask(__name__)
app.secret_key='zhenshirilegoule'
#login
@app.route('/login')
def login():
	return render_template('zuoye06_login.html')
#涉及到/tmp/python-reboot/6/template/zuoye06_display.html和zuoye06_login.html以及/tmp/python-reboot/6/user.txt和zuoye6.py文件
#login执行逻辑
@app.route('/login_action',methods=['post'])
def login_action():
	user=request.form.get('user')
	passwd=request.form.get('passwd')
	if user=='admin' and passwd=='admin':
		session['user']='admin'
	return redirect('/display')
#展示页面
@app.route('/display')
def display():
	if 'user' not in session:
		return redirect('/login')
	user_list=[]
	with open('user.txt') as f:
		for line in f:
			tmp=line.split(':')
			if len(tmp)==2:
				user_list.append(tmp)
	return render_template('zuoye06_display.html',user_web_list=user_list)
#添加用户
@app.route('/add',methods=['post'])
def add():
	user=request.form.get('user')
	passwd=request.form.get('passwd')
	if user=='' or passwd=='':
		return redirect('/display')
	f=open('user.txt','a+')
	f.writelines(user+':'+passwd+'\n')
	f.close()
	return redirect('/display')
#删除用户
@app.route('/delete',methods=['post'])
def delete():
	radio=request.form.get('radio')	
	user_list=[]
#读一遍user.txt文件，放入list
	with open('user.txt') as f:
		for line in f:
			tmp=line.split(':')
			if len(tmp)==2:
				user_list.append(tmp)
#对于页面传入的radio参数进行匹配并从list中删除
	for i in range(0,len(user_list)):
		if radio==user_list[i][0]:
			user_list.pop(i)
			break
#将pop后的list内容重新写入user.txt
	with open('user.txt','w') as f1:
		for j in range(len(user_list)):
			f1.writelines(user_list[j][0]+':'+user_list[j][1])
	return render_template('zuoye06_display.html',user_web_list=user_list)
#退出
@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/login')
if __name__=='__main__':
	app.run(host='0.0.0.0',port=9094,debug=True)
