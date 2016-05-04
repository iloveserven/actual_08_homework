#!/usr/bin/python27
#encoding=utf-8
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='ewrfdsafd43r43#%^%(*)()_njewqrewqrewq4$$%'
@app.route('/')
def index():
    if 'user' not in session:
        return redirect('login')
    username = 'admin'
    return render_template('index.html',username=username)

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
    if user == 'admin' and passwd == 'admin':
        session['user'] = 'admin'
    return redirect('/')

@app.route('/data')
def data():
    if 'user' not in session:
        return redirect('login')
    userlist = []
    with open('user.txt') as f:
        for line in f.readlines():
            tmp = line.strip().split(':')
            if len(tmp) == 2:
                userlist.append(tmp)
    return render_template('data.html',userlist=userlist)

@app.route('/adduser',methods=['post'])
def adduser():
    user =  request.form.get('user')
    passwd = request.form.get('passwd')
    user_dict = {}
    with open('user.txt') as f:
        for line in f.readlines():
            line = line.strip().split(':')
            user_dict[line[0]] = line[1]
    if user in user_dict:
        return u'%s已经存在，无法添加！' %user
    if len(user) == 0:
        return u"用户名不可以为空！"
    with open('user.txt','a') as f:
        f.write("%s:%s\n" %(user,passwd))
    return redirect('/data')

@app.route('/deluser',methods=['post'])
def deluser():
    user_dict = {}
    user = request.form.get('user')
    with open('user.txt') as f:
        for line in f.readlines():
            line = line.strip().split(':')
            user_dict[line[0]] = line[1]
    if user not in user_dict:
        return  u'%s不存在，无法删除!' %user
    else:
        del user_dict[user]

    with open('user.txt','w') as f:
        for key,val in user_dict.items():
            f.write('%s:%s\n'%(key,val))
    return redirect('/data')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9093,debug=True)
