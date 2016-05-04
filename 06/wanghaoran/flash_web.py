#coding=utf-8
import re
from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key='/sadsdfsfqwerqwersdfasdf-82371498432-1jafkjhsfasf'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	if 'user' not in session:
		return redirect('/login')
	userlist = []
	with open('user.txt') as f:
		for line in f:
			tmp = line.split(':')
			if len(tmp)==2:
				userlist.append(tmp)
	return render_template('data.html',userlist=userlist)
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
	user = request.form.get('user')
	passwd = request.form.get('passwd')
	if user=='admin' and passwd=='admin':
		session['user'] = 'admin'
	return redirect('/data')

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/login')

@app.route('/adduser',methods=['post']) 
def adduser():
	f = open('user.txt','a+')
	user = request.form.get('user')
	passwd = request.form.get('passwd')
	f.write('\n%s:%s' %(user,passwd))
	f.close
	return redirect('/data')

@app.route('/deluser',methods=['post']) 
def deluser():
	user = request.form.get('user')
	passwd = request.form.get('passwd')
	del_regex=re.compile('%s:%s' %(user,passwd))
	r = open('user.txt')
	if user not in r.read():
		return render_template('err.html')
	a = r.read()
	r.close()
	res = re.sub(del_regex,"",a)
	www = open('user.txt','w')
	www.write(res)
	www.close
	return redirect('/data')

if __name__=='__main__':
	app.run(host='0.0.0.0',port=9093,debug=True)