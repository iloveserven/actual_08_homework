#!/bin/env python
# coding=utf-8

from flask import Flask,session,redirect,render_template,request
import mysqldb
import user
import server
import access_log as a_log
import time
import json
import decimal
from sendemail import SendMail

db = mysqldb.DB()

app = Flask(__name__)
app.secret_key='asdfqwew987aakfa98&*^(asfqwer'


@app.route('/showtable')
def showtable():
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	if 'page_int' in session:
		page_int = session['page_int']
	else:
		page_int = 1
		session['page_int'] = page_int
	cur_url = request.base_url
	accesslist = a_log.access_log_list_by_page(page_int=page_int,page_size=page_size)
	accesslistcount = a_log.count_access_log()
	if accesslistcount%page_size == 0:
		page_num = accesslistcount/page_size
	else:
		page_num = accesslistcount/page_size + 1
	return json.dumps(a_log.access_log_list())
	# return render_template('logtable.html',accesslist=accesslist,page_int=int(page_int),page_num=int(page_num),page_size=int(page_size),cur_url=cur_url)


@app.route('/')
def index():
	if not 'user' in session:
	   return redirect('/login')
	is_admin = session['is_admin']
	username = session['user']
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	page_int = request.args.get('page_int')
	if not page_int:
		page_int = 1
	cur_url = request.base_url
	accesslist = a_log.access_log_list_by_page(page_int=page_int,page_size=page_size)
	accesslistcount = a_log.count_access_log()
	if accesslistcount%page_size == 0:
		page_num = accesslistcount/page_size
	else:
		page_num = accesslistcount/page_size + 1
	return render_template('index.html',accesslist=accesslist,username=username,is_admin=is_admin,page_int=int(page_int),page_num=int(page_num),page_size=int(page_size),cur_url=cur_url,current="loglist")


@app.route('/index')
def index1():
	if not 'user' in session:
	   return redirect('/login')
	is_admin = session['is_admin']
	username = session['user']
	cur_url = request.base_url
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	page_int = request.args.get('page_int')
	if not page_int:
		page_int = 1
	session['page_int'] = page_int
	return render_template('index1.html',username=username,is_admin=is_admin,cur_url=cur_url,current="loglist")


@app.route('/userlist')
def user_list1():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	username = session['user']
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	page_int = request.args.get('page_int')
	if not page_int:
		page_int = 1
	cur_url = request.base_url
	userlist = user.userlist_by_page(page_int=page_int,page_size=page_size)
	userlistcount = user.countuser()
	if userlistcount%page_size == 0:
		page_num = userlistcount/page_size
	else:
		page_num = userlistcount/page_size + 1
	return render_template('userlist.html',userlist=userlist,username=username,is_admin=is_admin,page_int=int(page_int),page_num=int(page_num),page_size=int(page_size),cur_url=cur_url,current="userlist")

@app.route('/userlist1')
def user_list():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	username = session['user']
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	page_int = request.args.get('page_int')
	if not page_int:
		page_int = 1
	cur_url = request.base_url
	userlist = user.userlist_by_page(page_int=page_int,page_size=page_size)
	userlistcount = user.countuser()
	if userlistcount%page_size == 0:
		page_num = userlistcount/page_size
	else:
		page_num = userlistcount/page_size + 1
	return render_template('userlist1.html',username=username,is_admin=is_admin,current="userlist")

@app.route('/serverlist')
def server_list():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	username = session['user']
	return render_template('serverlist.html',username=username,is_admin=is_admin,current="serverlist")

@app.route('/showserver')
def showserver():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	username = session['user']
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	page_int = request.args.get('page_int')
	if not page_int:
		page_int = 1
	cur_url = request.base_url
	return json.dumps(server.serverlist())

@app.route('/showuser')
def showuser():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	username = session['user']
	if 'page_size' in session:
		page_size = session['page_size']
	else:
		page_size = 10
		session['page_size'] = page_size
	page_int = request.args.get('page_int')
	if not page_int:
		page_int = 1
	cur_url = request.base_url
	return json.dumps(user.userlist())

@app.route('/userinfo')
def userinfo():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	userid = request.args.get('id')
	return json.dumps(user.user_by_id(userid))

class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return float(o)
		super(DecimalEncoder, self).default(o)

@app.route('/statuscount')
def statuscount():
	if not 'user' in session:
		return redirect('/login')
	return json.dumps(a_log.status_count(),cls=DecimalEncoder)


@app.route('/accessmap')
def accessmap():
	if not 'user' in session:
		return redirect('/login')
	res = a_log.access_log_list_with_geo()
	d_res = {}
	max_num = 0
	min_num = 0
	l_res = []
	for r in res:
		status = r['status']
		ip = r['ip']
		geox = r['geox']
		geoy = r['geoy']
		access_num = r['access_num']
		if access_num > max_num:
			max_num = access_num
		if min_num > access_num or min_num ==0:
			min_num = access_num
		l_res.append({'name':ip,'value':[geox,geoy,access_num]})
		# d_res[status]=d_res.get(status,[])+[{'name':ip,'value':[geox,geoy,access_num]}]
		d_res = {'min':min_num,'max':max_num,'data':l_res}
	return json.dumps(d_res)


@app.route('/accessflymap')
def accessflymap():
	if not 'user' in session:
		return redirect('/login')
	res = a_log.access_log_list_with_geo()
	res_r = {}
	res_l = []
	geos = {'200':[116.4551,40.2539],'404':[121.48,31.22],'304':[113.23,23.16]}
	for r in res:
		status = r['status']
		ip = r['ip']
		geox = float(r['geox'])
		geoy = float(r['geoy'])
		access_num = r['access_num']
		if access_num < 100:
			continue
		else:
			access_num /= 10
		tmp_data0 = [{'name':status,'coord':geos[status]},{'name':ip,'coord':[geox,geoy]}]
		tmp_data1 = [{'name':status,'coord':geos[status]},{'name':ip,'coord':[geox,geoy]}]
		tmp_data2 = [{'name':ip,'value':[geox,geoy,access_num]}]
		res_r[status] = res_r.get(status,{'data0':[],'data1':[],'data2':[]})
		res_r[status]['data0'].append(tmp_data0)
		res_r[status]['data1'].append(tmp_data1)
		res_r[status]['data2'] += tmp_data2
	for k,v in res_r.items():
		res_l.append([k,v])
	return json.dumps(res_l)


@app.route('/adduser',methods=['post'])
def adduser():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	name = request.form.get('name')
	password = request.form.get('password')
	email = request.form.get('useremail')
	count = user.adduser(name, password,email)
	if not count:
		return 'add user failed!'
	return redirect('/userlist')


@app.route('/adduser1',methods=['post','get'])
def adduser1():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	if request.method == 'POST':
		name = request.form.get('name')
		password = request.form.get('password')
		email = request.form.get('useremail')
	else:
		name = request.args.get('name')
		password = request.args.get('password')
		email = request.args.get('useremail')
	count = user.adduser(name, password,email)
	if not count:
		return 'error'
	return 'ok'


@app.route('/addserver',methods=['post','get'])
def addserver():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	if request.method == 'POST':
		name = request.form.get('name')
		memory = request.form.get('memory')
		expired_date = request.form.get('expired_date')
		email = request.form.get('email')
		note = request.form.get('note')
	else:
		name = request.args.get('name')
		memory = request.args.get('memory')
		expired_date = request.args.get('expired_date')
		email = request.args.get('email')
		note = request.args.get('note')
	count = server.addserver(name, memory, expired_date, email, note)
	if not count:
		return 'error'
	return 'ok'


@app.route('/deluser',methods=['get'])
def deluser():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	userid = request.args.get('userid')
	count = user.deluser(userid)
	if not count:
		return 'delete user failed!'
	return redirect('/userlist')


@app.route('/deluser1',methods=['get'])
def deluser1():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	userid = request.args.get('userid')
	count = user.deluser(userid)
	if not count:
		return 'error'
	return 'ok'


@app.route('/delserver',methods=['post'])
def delserver():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	serverid = request.form.get('serverid')
	count = server.delserver(serverid)
	if not count:
		return 'error'
	return 'ok'


@app.route('/deluser2',methods=['post'])
def deluser2():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	userid = request.form.get('userid')
	res = user.user_by_id(userid)
	name = res['name']
	password = res['password']
	email = res['email']
	m = SendMail('Delete account %s'%name ,'name:%s email:%s was delete.'%(name,email),'%s<%s>'%(name,email))
	m.send_mail()
	count = user.deluser(userid)
	if not count:
		return 'error'
	return 'ok'


@app.route('/edituser',methods=['get'])
def edituser():
	if not 'user' in session:
		return redirect('/login')
	username = session['user']
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	userid = request.args.get('userid')
	user_info = user.user_by_id(userid)
	return render_template('useredit.html',user_info=user_info,username=username,is_admin=is_admin,current="userlist")


@app.route('/edituseraction',methods=['post'])
def edituseraction():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	userid = request.form.get('userid')
	password = request.form.get('password')
	email = request.form.get('useremail')
	count = user.edituser(userid,password,email)
	if not count:
		return 'error'
	return redirect('/userlist')


@app.route('/editserveraction',methods=['post'])
def editserveraction():
	if not 'user' in session:
		return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	serverid = request.form.get('serverid')
	name = request.form.get('name')
	memory = request.form.get('memory')
	expired_date = request.form.get('expired_date')
	email = request.form.get('email')
	note = request.form.get('note')
	count = server.editserver(serverid, name, memory, expired_date, email, note)
	if not count:
		return 'error'
	return 'ok'


@app.route('/changepagesize',methods=['post'])
def changepagesize():
	if not 'user' in session:
		return redirect('/login')
	cur_url = request.form.get('cur_url')
	page_size = request.form.get('page_size')
	if not page_size:
		page_size = 10
	session['page_size'] = int(page_size)
	return redirect(cur_url)


@app.route('/statistics',methods=['post'])
def statistics():
	if not 'user' in session:
	   return redirect('/login')
	is_admin = session['is_admin']
	if not is_admin:
		return redirect('/index')
	top_num = request.form.get('top_num')
	a_log.get_max_many(max_many=int(top_num))
	a_log.del_all()
	a_log.insert_access()
	return redirect('/index')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/loginaction',methods=['post','get'])
def loginaction():
	is_admin = 0
	is_exist_user = 0
	username = request.form.get('username')
	password = request.form.get('password')
	sql = "select password from user where name='%s' and password='%s'"%(username,password)
	res = db.select_one(sql)
	if res:
		if res['password'] == password:
		   is_exist_user = 1
		   session['user'] = username
		if username == 'admin' and password == 'admin':
		   is_admin = 1
		session['is_admin'] = is_admin
		if is_exist_user:
		   return redirect('/index')
		else:
		   return redirect('/login')
	else:
		return redirect('/login')


@app.route('/logout')
def logout():
	session.pop('user')
	session.pop('is_admin')
	return redirect('/login')


if __name__=='__main__':
	app.run(host='0.0.0.0',port=80,debug=True)