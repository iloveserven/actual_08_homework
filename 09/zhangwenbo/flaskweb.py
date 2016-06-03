#encoding=utf-8

from flask import Flask,render_template,request,redirect,session 
# import MySQLdb as mysql
# con = mysql.connect(db='web',host='localhost',user='root',passwd='mysql')
# con.autocommit(True)
# cursor = con.cursor()

import dbutil
import json
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
        # page = int(request.args.get('page',0))
        # count = request.args.get('count',10)
        # if 'user' not in session:
        #     return redirect('/login')
        # sql = 'select * from log limit %s,%s' % (int(page)*int(count),count)
        # ip_list = dbutil.execute(sql)
        # return render_template('ip_list.html',ip_list=ip_list,page=page)
        # page = int(request.args.get('page')
        if 'user' not in session:
            return redirect('/login')
        sql = 'select * from log'
        ip_list = dbutil.execute(sql)
        return render_template('ip_list.html',ip_list=ip_list)

 
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


 
@app.route('/adduser',methods=['post']) 
def adduser(): 
        user = request.form.get('user') 
        password = request.form.get('password') 
        if user =="" or password =="":
            return "error"
        sql = 'insert into user (username,password) values ("%s","%s")' % (user,password)
        try:
            dbutil.execute(sql)
        except:
            return "error,please view python"
        else: 
            return 'ok' 

@app.route('/delete')
def delete():
        id = request.args.get('id')
        sql1 = 'delete from user where id=%s' % (id)
        dbutil.execute(sql1)
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
