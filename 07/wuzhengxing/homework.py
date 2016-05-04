import MySQLdb as mysql
from flask import Flask,render_template,request,redirect,session
import home

app =Flask(__name__)
app.secret_key = '/sad/abc@@123'
cursor = con.cursor()


@app.route('/')
def index():
        if session.get('user',0) == 0:
                return redirect('/login')
        flag = request.args.get('flag')
        cursor.execute('select * from log')
        res1 = cursor.fetchall()
        cursor.execute('select * from log order by counttime')
        res2 = cursor.fetchall()
        if flag ==  '0':
                return render_template('index.html',userlist=res2,user=session['user'])
        else:
                return render_template('index.html',userlist=res1,user=session['user'])


@app.route('/login_action',methods=['post','get'])
def login_action():
        user = request.form.get('name')
        passwd = request.form.get('passwd')
        if cursor.fetchall()[0][0] == 0:
                return render_template('login.html')
        else:
                session['user'] = user
                return redirect('/')

@app.route('/login')
def login():
        return render_template('/login.html')

@app.route('/user')
def user():
        if not session.get('user',0) or session.get('user',0)!='admin':
                return redirect('/login')
        cursor.execute('select * from user')
        return render_template('/user.html',userlist=cursor.fetchall())

@app.route('/out')
def out():
        return redirect('/')

@app.route('/logout')
def logout():
        session.pop('user')
        return redirect('login')


@app.route('/addusers',methods=['POST'])
def addusers():
        user=request.form.get('user')
        pwd=request.form.get('pwd')
        cursor.execute('insert into user (user,passwd) values ("%s","%s")'%(user,pwd))
        return redirect('/user')


@app.route('/delusers')
def defusers():
        id = request.args.get('id')
        cursor.execute('delete from user where id="%s"'%(id))
        return redirect('/user')


@app.route('/updateusers',methods=['post'])
def upodateusers():
        uid=request.form.get('id')
        pwd=request.form.get('pwd')
        print uid,pwd
        cursor.execute("update user set  passwd='%s' where id='%s'"%(pwd,uid))
        return redirect('/user')

if __name__=='__main__':
        app.run(host='0.0.0.0',port=10001,debug=True)
