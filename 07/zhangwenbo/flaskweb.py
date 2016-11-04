#encoding=utf-8

from flask import Flask,render_template,request,redirect,session 
import MySQLdb as mysql
con = mysql.connect(db='web',host='localhost',user='root',passwd='mysql')
con.autocommit(True)
cursor = con.cursor()

app = Flask(__name__) 
app.secret_key='sddddfrg4thdnaindi2398r2idnao01nidsnoi12ni' 
 
@app.route('/') 
def index(): 
        return render_template('index.html') 
 
@app.route('/data') 
def user_01(): 
        if 'user' not in session: 
            return redirect('/login') 
        cursor.execute('select * from user')
        return render_template('data.html',userlist=cursor.fetchall())


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
        cursor.execute('select * from log')
        return render_template('ip_list.html',ip_list=cursor.fetchall())
 
@app.route('/loginaction',methods=['post']) 
def loginaction(): 
        user = request.form.get('user') 
        passwd = request.form.get('passwd')
        sql = "select * from user where username='%s' and password='%s'" % (user,passwd)
        cursor.execute(sql)
        tp = cursor.fetchall()
        if not tp:
            return redirect('/login')
        else:
            if tp[0][1]=='admin' and tp[0][2]=='admin':             
                session['user'] = 'admin' 
                return redirect('/data')
            else:
                session['user'] = user
                return redirect('/ip_list')

 
@app.route('/adduser',methods=['post']) 
def adduser(): 
        user = request.form.get('user') 
        password = request.form.get('password') 
        sql = 'insert into user (username,password) values ("%s","%s")' % (user,password)
        try:
            cursor.execute(sql)
        except:
            return "error,please view python"
        else: 
            return redirect('/login') 

@app.route('/delete',methods=['post'])
def delete():
        id = request.form.get('id')
        sql1 = 'delete from user where id=%s' % (id)
        cursor.execute(sql1)
        return redirect('/data')

@app.route('/edit',methods=['post'])
def edit():
        id = request.form.get('id')
        password = request.form.get('passwd') 
        sql = 'update user set password="%s" where id=%s '% (password,id)
        try:
            cursor.execute(sql)
        except:
            return "please enter passwd"
        else:
            return redirect('/data')

 
if __name__ == '__main__': 
        app.run(host='0.0.0.0',port=10000,debug=True)
