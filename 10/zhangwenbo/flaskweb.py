#encoding=utf-8

from flask import Flask,render_template,request,redirect,session 
# import MySQLdb as mysql
# con = mysql.connect(db='web',host='localhost',user='root',passwd='mysql')
# con.autocommit(True)
# cursor = con.cursor()

import dbutil
import smtp
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__) 
app.secret_key='sddddfrg4thdnaindi2398r2idnao01nidsnoi12ni' 
 
@app.route('/') 
def index(): 
        return render_template('login.html') 
 
@app.route('/data') 
def user_01(): 
        if 'user' not in session: 
            return redirect('/login') 
        ulst = dbutil.execute('select * from user')
        return render_template('data.html',userlist=ulst)


@app.route('/login') 
def login(): 
        return render_template('login.html') 
 
@app.route('/logout') 
def logout(): 
        session.pop('user') 
        return redirect('/login') 

@app.route('/ip_list')
def list():
        if 'user' not in session:
            return redirect('/login')
        sql = 'select * from log'
        ip_list = dbutil.execute(sql)
        return render_template('ip_list.html',ip_list=ip_list)

@app.route('/logecharts')
def logecharts():
        return render_template('echarts.html')

@app.route('/loghttp')
def loghttp():
        sql = 'select * from log'
        ip_data = dbutil.execute(sql)
        log_pre = {}
        for log in ip_data:
            log_pre[log[2]] = log_pre.get(log[2],0)+log[3]
        res = {'legend':[],'data':[]}
        for status,count in log_pre.items():
            status = str(status)
            res['legend'].append(status)
            res['data'].append({'name':status,'value':count})
        return json.dumps(res)

@app.route('/log_map')
def log_map():
        return render_template('log_map.html')

@app.route('/logmap')
def logmap():
        sql = 'select * from log_map'
        sql1 = 'select max(count),min(count) from log_map'
        ip_data = dbutil.execute(sql)
        mm = dbutil.execute(sql1)
        res = {'data':[],'ma':[],'mi':[]}
        for mp in ip_data:
            res['data'].append({'name':mp[0],'value':[mp[2],mp[3],mp[4]]})
        for mx in mm:
            res['ma']= mx[0]
            res['mi']= mx[1]
        return json.dumps(res)



@app.route('/loginaction',methods=['post']) 
def loginaction(): 
        user = request.form.get('user') 
        passwd = request.form.get('passwd')
        sql = "select * from user where username='%s' and password='%s'" % (user,passwd)
        tp = dbutil.execute(sql)
        if not tp:
            return redirect('/login')
        else:
            if tp[0][1]=='admin' and tp[0][2]=='admin':             
                session['user'] = 'admin' 
                return redirect('/data')
            else:
                session['user'] = user
                return redirect('/ip_list')

@app.route('/gettable')
def gettable():
    sql = 'select * from user order by id'   
    res = json.dumps(dbutil.execute(sql))
    return res

@app.route('/host')
def host():
    return render_template('source.html')

@app.route('/hostlist')
def hostlist():
    if 'user' not in session:
        return redirect('/login')
    sql = 'select * from host'   
    hostlist = json.dumps(dbutil.execute(sql))
    return hostlist

@app.route('/addhost',methods=['post'])
def addhost():
        host1= request.form.get('host1')
        host2= request.form.get('host2')
        host3= request.form.get('host3')
        host4= request.form.get('host4')
        if host1 =="" or host2=="" or host3=="" or host4=="":
            return 'error'
        sql= 'insert into host (hostname,memory,losetime,email) values ("%s","%s","%s","%s")' % (host1,host2,host3,host4)
        try:
            dbutil.execute(sql)
        except:
            return "error,please view python"
        else: 
            return 'ok'

@app.route('/deletehost',methods=['post'])
def deletehost():
        id = request.form.get('id')
        sql1 = 'delete from host where id=%s' % (id)
        dbutil.execute(sql1)
        return 'ok'

@app.route('/updatehost',methods=['post'])
def updatehost():
        id = request.form.get('id')
        h1 = request.form.get('h1')
        h2 = request.form.get('h2')
        h3 = request.form.get('h3')
        h4 = request.form.get('h4')
        if id=="" or h1 =="" or h2=="" or h3=="" or h4=="":
            return 'error'
        sql = 'update host set hostname="%s",memory="%s",losetime="%s",email="%s" where id=%s '% (h1,h2,h3,h4,id)
        try:
            dbutil.execute(sql)
        except:
            return "please enter passwd"
        else:
            return 'ok'        

@app.route('/adduser',methods=['post']) 
def adduser(): 
        user = request.form.get('user') 
        password = request.form.get('password') 
        if user =="" or password =="" or " " in user or " " in password:
            return "error"
        sql = 'insert into user (username,password) values ("%s","%s")' % (user,password)
        try:
            dbutil.execute(sql)
        except:
            return "error,please view python"
        else: 
            return 'ok' 

@app.route('/delete',methods=['post'])
def delete():
        id = request.form.get('id')
        sql1 = 'delete from user where id=%s' % (id)
        dbutil.execute(sql1)
        smtp.autosendmail(id)
        return 'ok'

@app.route('/edit',methods=['post'])
def edit():
        id = request.form.get('id')
        password = request.form.get('pwd') 
        print id,password
        if password == "":
            return 'error'
        sql = 'update user set password="%s" where id=%s '% (password,id)
        try:
            dbutil.execute(sql)
        except:
            return "please enter passwd"
        else:
            return 'ok'

if __name__ == '__main__': 
        app.run(host='0.0.0.0',port=10000,debug=True)
