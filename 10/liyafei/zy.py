#!/usr/bin/python
# coding=utf-8
import MySQLdb as mysql
from flask import Flask,render_template,request,redirect,session
import sql,json,config
app=Flask(__name__)
app.secret_key='adsfasdf90239rkdsakKSDANFOAKDNFKADSNFKASDFNKADFKLDASLFK'
db = sql.DB(config.db,config.db_host,config.db_user,config.db_passwd)

@app.route('/')
def index():
    if 'user'  not in session:
        return render_template('login.html')
    else:
        if session['user'] == 'admin':
            return redirect('/data')
        else:
            return redirect('/datauser')
@app.route('/loginaction',methods=['post'])
def loginaction():
    try:
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        sql = 'select * from user where username="%s"' % user 
        userinfo = db.execute(sql)
        dbuser = userinfo[0][1]
        dbpwd = userinfo[0][2]

        if (user.strip() == dbuser and passwd.strip()==dbpwd) and dbuser == 'admin':
            session['user'] = dbuser
            return redirect('/data')
        elif user.strip() == dbuser and passwd.strip()==dbpwd:
            session['user'] = dbuser
            return redirect('/datauser')
        else:
            return render_template('error.html')
    except:
        return render_template('error.html')
@app.route('/loginout')
def loginout():
    if 'user' in session:
        session.pop('user')
        return redirect('/')
    else:
        return redirect('/')
@app.route('/data')
def data():
    if 'user' in session and session['user'] == 'admin':
        sql = 'select * from data'
        s_list = db.execute(sql)
        name=session['user']
        return render_template('data.html',userlist=s_list,name=name)
    else:
        return redirect('/')

@app.route('/mes_data')
def mes_data():
    if 'user' in session and session['user'] == 'admin':
        sql = 'select * from mes_data'
        s_list = db.execute(sql)
        name=session['user']
        return render_template('mes_data.html',userlist=s_list,name=name)
    else:
        return redirect('/')

@app.route('/userlist')
def userlist():
    if 'user' in session and session['user'] == 'admin':
        sql = 'select * from user'
        u_list = db.execute(sql)
        name=session['user']
        return render_template('userlist.html',userlist=u_list,name=name)  
    else:
        return redirect('/')

@app.route('/add_mesdata',methods=['post'])
def add_mesdata():
    hostinfo = request.form.get('hostinfo')
    memsize = request.form.get('memsize')
    cpunum = request.form.get('cpunum')
    email = request.form.get('email')
    dataago = request.form.get('dataago')
    textinput = request.form.get('textinput')
    if len(hostinfo) and len(memsize) and len(cpunum) and len(email) and len(dataago) and len(textinput) != '':

        sql = "insert into mes_data(host_info,mem_info,cpu_inof,mail_info,date_info,rmk_info) values ('%s','%s','%s','%s','%s','%s')" % (hostinfo, memsize, cpunum, email, dataago, textinput)
        print sql
        db.execute(sql)
        return 'ok'
    else:
        return 'not'

@app.route('/adduser')
def adduser():
    try:
        user= request.args.get('user')
        pwd = request.args.get('pwd')
        user = user.strip()
        pwd = pwd.strip()
        if len(user) and len(pwd) != '':
            sql = "insert into user (username,password) values (\'%s\',\'%s\')" % (user,pwd)
            db.execute(sql)
            return 'ok'
        else:
            return 'not'
    except:
        return "添加失败,请检查！"
@app.route('/updateuser',methods=['post'])
def updateuser():
    try:
        idnum =  request.form.get('id')
        pwd =  request.form.get('pwd')
        pwd = pwd.strip()
        sql = "update user set password='%s' where id='%s'" % (pwd,idnum)
        print sql
        db.execute(sql)
        return 'ok'
        return redirect('/userlist')
    except:
        return "修改失败,请检查！"
@app.route('/deluser',methods=['post'])

@app.route('/update_mesdata',methods=['post'])
def update_mesdata():

    idnum =  request.form.get('id')
    hostinfo = request.form.get('hostinfo')
    memsize = request.form.get('memsize')
    cpunum = request.form.get('cpunum')
    email = request.form.get('email')
    dataago = request.form.get('dataago')
    textinput = request.form.get('textinput')
    if len(hostinfo) and len(memsize) and len(cpunum) and len(email) and len(dataago) and len(textinput) != '':
        
       # sql = "insert into mes_data(host_info,mem_info,cpu_inof,mail_info,date_info,rmk_info) values ('%s','%s','%s','%s','%s','%s')" % (hostinfo, memsize, cpunum, email, dataago, textinput)
        sql = "update mes_data set host_info='%s',mem_info='%s',cpu_inof='%s',mail_info='%s',date_info='%s',rmk_info='%s' where id='%s' " % (hostinfo, memsize, cpunum, email, dataago, textinput ,idnum)
        print sql
        db.execute(sql)
        return 'ok'
    else:
        return 'not'

def deluser():
    try:
        idnum =  request.form.get('id')
        sql = 'select username from user  where id=%s' % idnum
        tmp = db.execute(sql)
        user_id =tmp[0][0]
        if user_id.strip() == 'admin':
            return "Sorry ,此用户不能删除，请返回!"
        else:
            sql = 'delete from user where id=%s' % idnum
            print sql
            db.execute(sql)
            return 'ok'
    except:
        return "删除用户失败，请检查！"
@app.route('/del_mesdata',methods=['post'])
def del_mesdata():
    idnum =  request.form.get('id')
    sql = 'delete from mes_data where id=%s' % idnum
    print sql
    db.execute(sql)
    return 'ok'
@app.route('/datauser')
def datauser():
    if 'user' in session and session['user'] != 'admin':
        sql = 'select count(*) from data'
        db.execute(sql)
        name=session['user']
        return render_template('user.html',userlist=s_list,name=name)
    else:
        return redirect('/')

@app.route('/gettable')
def gettable():
    if 'user' in session and session['user'] == 'admin':
        sql = 'select * from user'
        u_list = db.execute(sql)
        res = json.dumps(u_list)
        print res
        return res
    else:
        return redirect('/') 
@app.route('/getmesdata')
def getmesdata():
    if 'user' in session and session['user'] == 'admin':
        sql = 'select * from mes_data'
        u_list = db.execute(sql)
        res = json.dumps(u_list)
        print res
        return res
    else:
        return redirect('/')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

