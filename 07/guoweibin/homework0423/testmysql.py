# -*- coding: utf-8 -*-
import MySQLdb as mysql
from flask import Flask,render_template,request,redirect,session
import logdata 



app=Flask(__name__)

con  =  mysql.connect(user='root',passwd='123456',db='guoweibin',host='localhost')
con.autocommit(True)
cursor = con.cursor()

app.secret_key='/sad/ikhkj?jklhd-908182903jk43-42348038401'


  
@app.route('/')
def index():
         sql  =  'select  *  from user  '
         print  request.args

         if  request.args.get('order ')=='desc':
         	sql += '   order by id desc'
         print cursor.execute(sql)
         return render_template('index.html',userlist=cursor.fetchall())

@app.route('/login',methods=['get','post'])
def  login():
	if  'user '  in session:
		return redirect('/')
	else:
		print request.method
		if  request.method=='GET':
			return render_template('log.html')
		elif  request.method=="POST":
                                                username = request.form.get('username')
                                                password  =request.form.get('passwd')
                                                if username=='admin' and password=='admin':
                                                         sql='select  *  from user  where username="%s" and password="%s" '%(username,password)
                                                         cursor.execute(sql)
                                                         if  cursor.fetchall():
                                                              session['username']='admin'
                                                              sql= 'select  * from  user'
                                                              cursor.execute(sql)
                                                              return render_template('index.html',userlist=cursor.fetchall())
                                                         else:
                                                         	return redirect('/login')

                                                else:
                                                               sql='select  *  from user  where username="%s" and password="%s" '%(username,password)
                                                               cursor.execute(sql)
                                                               if cursor.fetchall():
                                                                              return redirect('/loglist')
                                                               else:
                                                                	return redirect('/login')

@app.route('/logout')
def logout():
	# session.pop('username')
	return redirect('/login')

@app.route('/loglist')
def logshow():
	logdata.logacess('www_access_20140823.log')

	#分页显示日志
	page=int(request.args.get('page',1))
	num=5

	cursor.execute("select  count(*)  from  logdb")
	total=cursor.fetchone()[0]
	print total
	if  total%num==0:
		pages=total/num
	else:
		pages=total/num+1
	start_position=(page-1)*num
	cursor.execute('select * from logdb limit  %s, %s '%(start_position,num))
	data=cursor.fetchall()
	print data
	return render_template('loglist.html',log_list=data,pages=pages)
	
	# return  render_template('loglist.html',log_list=cursor.fetchall())

@app.route('/adduser',methods=['post'])
def  adduser():
 	username=request.form.get('user')
 	passwd = request.form.get('password')
 	sql='insert into user  (username,password) values("%s","%s") '%(username,passwd)
 	try:
 		cursor.execute(sql)
 	except:
 		return 'Error'
 	else:
 	             return    redirect('/')

@app.route('/deluser')
def deluser():
	username = request.args.get('username')
	##将admin限定不能删除
	if  username=='admin':
		return redirect('/')
	else:
                         sql='delete from user where  username="%s" '  % (username)
                         cursor.execute(sql)
                         return redirect('/')

	# cursor.execute(sql)
	# return  redirect('/')


@app.route('/update')
def update():
	id=request.args.get('id')	
	newpassword=request.args.get('newpassword')
	sql='update user set password="%s" where  id="%s" '%(newpassword,id)
	cursor.execute(sql)
	return redirect('/')

if   __name__=='__main__':
	app.run(host='127.0.0.1',port=9093,debug=True)




