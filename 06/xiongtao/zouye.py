
#coding:utf-8
#redirect 
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='dnaindi2398r2idnao01nidsnoi12ni'

@app.route('/')
def index():
       username = 'admin'
       return render_template('index011.html',username=username)

@app.route('/lixiaolong')
def lixiaolong():
       if 'user' not in session:
                return redirect('/login')
       userlist = []
       with open('./userss.txt') as f:
                for line in f:
                      tmp = line.split(':')
                      if  len(tmp) == 2:
                            userlist.append(tmp)
       return render_template('lixiaolong.html',userlist=userlist)

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/logout')
def logout():
        session.pop('user')
        return redirect('/login')

@app.route('/loginaction',methods=['post'])
def loginaction():
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        if user=='admin'and passwd=='admin':
                session['user'] = 'admin'
                return redirect('/lixiaolong')

@app.route('/adduser',methods=['post'])
def adduser():
        print request.args
        user = request.form.get('user')
        password = request.form.get('password')
        with open('./userss.txt','a') as f:
                f.write('\n'+user+':'+password)
        return redirect('/lixiaolong')

@app.route('/Duser',methods=['post'])
def Deuser():
    user = request.form.get('user')
    if user:
          with open('./userss.txt','r') as f:
                tmplist=f.readlines()
          with open('./userss.txt','w') as file_:
                for line in tmplist:
                        line_ = line.split()
                        user_ = line.split()
                        if line_ == user_:
                            continue
                        else:
                                file_.write(line)
          return redirect('/lixiaolong')
    return "deletenum"


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=9999,debug=True)
