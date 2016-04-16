#!/usr/bin/python

from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = '/sad/abc@@123'

@app.route('/')
def index():
	return redirect('/show')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/loginact',methods=['post'])
def loginact():
	name = request.form.get('name')
	passwd = request.form.get('passwd')
	if name == 'admin' and passwd == 'admin':
		session['user'] = 'admin'
		return redirect('/show')
	return redirect('/login')

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/login')

@app.route('/show')
def show():
	if 'user' not in session:
		return redirect('/login')
	user_lst = []
	with open('user.txt','r') as f:
		for line in f:
			tmp = line.split(':')
			if len(tmp) == 2:
				user_lst.append(tmp)
	return render_template('index.html',res_lst=user_lst)

@app.route('/add',methods=['post'])
def add():
	name = request.form.get('name')
	passwd = request.form.get('passwd')
	with open('user.txt','a') as f:
		f.write('\n'+name+':'+passwd)
	return redirect('/show')

@app.route('/dele',methods=['post'])
def dele():
	tmp_dict = {}
	tmp_lst = []
	name = request.form.get('name')
	with open('user.txt','r') as f:
		for line in f:
			tmp = line.split(':')
			if len(tmp) == 2 and tmp[0] != name:
				tmp_dict[tmp[0]] = tmp[1]	
				tmp_lst.append(tmp)
	with open('user.txt','w') as f:	
		for i in tmp_lst:
			for key,val in tmp_dict.items():
				if i[0] == key:
					f.write(key+':'+val)
	return redirect('/show')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=10086,debug=True)
