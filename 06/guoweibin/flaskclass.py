# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='112233'

@app.route('/')
def index():
    
    return render_template('login.html')

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
    password=request.form.get('passwd')
    if user=='admin' and password=='admin':
        session['user']='admin'
    return redirect('/data')

#####读取文件的数据，并展示在浏览器前端
@app.route('/data')
def data():
    if 'user' not in session:
        return redirect('/login')
    userlist=[]
    with open('user.txt') as f:
       for line in f:
           tmp=line.strip().split(':')
           if len(tmp)==2:
               userlist.append(tmp)

    return render_template('data.html',userlist=userlist)

@app.route('/adduser',methods=['POST'])
def adduser():
##get()括号的内容要和前端的name属性值保持一致
    if 'user' not in session:
        return redirect('/login')
    user=request.form.get('username')
    password=request.form.get('password')

    if not user or not password:
        return redirect('/data')
    with open('user.txt','a') as f:
        f.write('\n'+user+':'+password)
    return redirect('/data')

@app.route('/deluser')
def deluser():
    if 'user' not in session:
        return redirect('/login')
    username=request.args.get('username')
    print username
    user_list=[]
    with open('user.txt') as f:
            for line in f:
                if len(line.strip().split(':'))==2:
                    user_list.append(line.strip().split(':'))
    for _str in user_list:
        if _str[0]==username:
           user_list.remove(_str)

    with open('user.txt','w') as _file:
        for str in user_list:
            _file.write('\n'+str[0]+':'+str[1])

    return redirect('/data')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=9002,debug=True)

