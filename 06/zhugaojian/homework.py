#!/bin/env python
# coding=utf-8

from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key='saf98714lknmsaf988u12*0124\sqr'

@app.route('/')
def index():
    return render_template('login.html')

# 用户列表
@app.route('/userlist')
def userlist():
    if 'user' not in session:
        return redirect('/login')
    user_list = []
    with open('user.txt') as f:
        for i in f.readlines():
            if len(i.strip().split(':')) == 2:
                user_list.append(i.strip().split(':'))
    return render_template('userlist.html',user_list=user_list)

# 添加用户，不验证用户名是否重复
@app.route('/useradd',methods=['post','get'])
def user_added():
    # 判断是否登录
    if 'user' not in session:
        return redirect('/login')
    name = request.form.get('name')
    password = request.form.get('password')
    # 用户名或者密码是否为空则不添加
    if not name or not password:
        return redirect('/userlist')
    with open('user.txt','a') as f:
        f.writelines('\n'+name+':'+password)
    return redirect('/userlist')

# 删除用户，相同用户名密码数据只删除一个
@app.route('/userdel',methods=['post','get'])
def user_del():
    if 'user' not in session:
        return redirect('/login')
    # 防止不选择导致出错
    if not request.form.get('name'):
        return redirect('/userlist')
    name_list = request.form.get('name').split('_')
    file_str = ''
    user_list = []
    with open('user.txt') as f:
        for line in f:
            if len(line.strip().split(':')) == 2:
                user_list.append(line.strip().split(':'))
    user_list.remove(name_list)
    print name_list
    print user_list
    for i in user_list:
        file_str += '\n'+':'.join(i)
    with open('user.txt','w') as f:
        f.writelines(file_str[1:])
    return redirect('/userlist')

# 登录页
@app.route('/login')
def login():
    if 'user' in session:
        return redirect('/userlist')
    return render_template('login.html')

# 用户登录
@app.route('/loginaction',methods=['post','get'])
def loginaction():
    name = request.form.get('name')
    password = request.form.get('password')
    print 'name:'+name+'  password:'+password
    if name=='admin' and password=='admin':
        session['user']=name
    return redirect('/userlist')

# 用户退出
@app.route('/logout',methods=['get','post'])
def logout():
    session.pop('user')
    return redirect('/login')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9093,debug=True)
