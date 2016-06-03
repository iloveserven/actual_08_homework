#!/usr/bin/env python
#coding=utf-8
from flask import Flask, render_template,request,redirect,session
app=Flask(__name__)
import dbutil
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import config
db = dbutil.DB(config.db,config.db_host,config.db_user,config.db_passwd)

app.secret_key='asjkdhk123908789123-0329-kladjklklj??=-123'

@app.route('/login',methods=['get','post'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        user = request.form.get('ur')
        pwd = request.form.get('pw')
        if user=='admin' and pwd=='admin':
            session['user']='admin'
            return 'ok'
        else:
            sql = 'select * from user where username="%s" and password="%s"'%(user,pwd)
            res = db.execute(sql)
            if len(res)>0:
                session['user'] = user
                return 'ok'
            else:
                return 'error'

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect('/login')

@app.route('/')
def index():
    if 'user' in session:
        if session['user']=='admin':
            res = 'select * from user'
            username = session['user']
            return render_template('index.html',userlist=res,username=username)
        else:
            return redirect('/zichan') 
    else:
        return redirect('/login')

@app.route('/adduser',methods=['POST'])
def adduser():
    user = request.form.get('user')
    pwd = request.form.get('pwd')
   # print request.method
    print user,pwd
    if user != '' and pwd != '' and ' ' not in user and ' ' not in pwd:
        sql='insert into user (username,password) values ("%s","%s")' %(user,pwd)
        print sql
        try:
            db.execute(sql)
        except:
            return 'error'
        else:
            return 'ok'
    else:
        return 'error'

@app.route('/deluser')
def deluser():
    if 'user' in session:
        id = request.args.get('id')
        sql= 'delete from user where id=%s' %(id)
        db.execute(sql)
        return 'ok'
    else:
        return 'you must login'
@app.route('/updateuser',methods=['POST'])
def updateuser():
    if 'user' in session:
        id = request.form.get('id')
        pwd = request.form.get('pwd')
        sql = 'update user set password="%s" where id=%s'%(pwd,id)
       # print sql
       # print id
        db.execute(sql)
        return 'ok'
    else:
        return 'you must login'

@app.route('/log')
def log():
    if 'user' in session:
        page = int(request.args.get('page',0))
        count = request.args.get('count',10)
        sql = 'select * from log limit %s,%s'%(int(page)*int(count),count)
        res = db.execute(sql)
        username = session['user']
        return render_template('log.html',logs=res,page=page,username=username)
    else:
        return redirect('/login')

@app.route('/lianxifs')
def lianxifs():
    return render_template('lianxifs.html')

@app.route('/gettable')
def gettable():
    if 'user' in session:
        sql = 'select * from user order by id'
        res = json.dumps(db.execute(sql))
        #print res
        return res
    else:
        return 'you must login'

@app.route('/zichan')
def zichan():
    if 'user' in session:
        username=session['user']
        return render_template('zichan.html',username=username)
    else:
        return 'you must login'

@app.route('/getzichan')
def getzichan():
    if 'user' in session:
        sql = 'select * from zichan order by id'
        res = json.dumps(db.execute(sql))
        #print res
        return res
    else:
        return 'you must login'

@app.route('/addhost',methods=['POST'])
def addhost():
    hn = request.form.get('hn')
    cpu = request.form.get('cpu')
    mem = request.form.get('mem')
    exdate = request.form.get('exdate')
    author = request.form.get('author')
    note = request.form.get('note')
    sql='insert into zichan (hostname,cpu,mem,exdate,author,note) values ("%s","%s","%s","%s","%s","%s")' %(hn,cpu,mem,exdate,author,note)
    print sql
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/delhost')
def delhost():
    if 'user' in session:
        id = request.args.get('id')
        sql= 'delete from zichan where id=%s' %(id)
        db.execute(sql)
        return 'ok'
    else:
        return 'you must login'

@app.route('/updatehost',methods=['POST'])
def updatehost():
    if 'user' in session:
        id = request.form.get('id')
        hostname = request.form.get('hostname')
        cpu = request.form.get('cpu')
        mem = request.form.get('mem')
        exdate = request.form.get('exdate')
        author = request.form.get('author')
        note = request.form.get('note')
        sql = 'update zichan set hostname ="%s",cpu ="%s",mem ="%s",exdate ="%s",author ="%s",note ="%s" where id=%s'%(hostname,cpu,mem,exdate,author,note,id)
       # print sql
       # print id
        db.execute(sql)
        return 'ok'
    else:
        return 'you must login'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=1212,debug=True)
