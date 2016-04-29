#coding:utf-8

from flask import Flask,render_template,redirect,request,session

import models

app = Flask(__name__)
app.secret_key = 'ytugiuhjhfjhjh'

@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html',datalist=models.show_info())
	else:
		return redirect('/login')

@app.route('/users')
def users():
	if 'uu' in session:
		return render_template('users.html',userlist=models.show_users())
	else:
		return redirect('/login')

@app.route('/login',methods=["post","get"])
def login():
	if 'username' in session:
		return redirect('/')
	else:
		if request.method == 'GET':
			return render_template('login.html')
		elif request.method == 'POST':
			username = request.form.get('username')
			password = request.form.get('password')
			print username,password
			if username == 'admin':
				session['uu'] = 'admin'
			if models.login(username,password):
				session['username'] = 'ok'
				return redirect('/')
			else:
				return 'username or password wrong'

@app.route('/logout')
def logout():
	#session.pop('username')	
	session.clear()
	return redirect('/login')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=9010,debug=True)
