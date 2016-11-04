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
    user_dict = {}
    with open('user.txt') as f:
        for i in f.readlines():
            tmp = i.strip().split(':')
            if len(tmp) == 2:
                user_dict[tmp[0]] = tmp[1]
    return render_template('userlist.html',user_list=user_dict.items())

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
    user_dict = {}
    with open('user.txt') as f:
        for i in f.readlines():
            tmp = i.strip().split(':')
            if len(tmp) == 2:
                user_dict[tmp[0]] = tmp[1]
    if name in user_dict:
        return "user exist <a href='/userlist'>返回</a>"
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
    name = request.form.get('name')
    user_dict = {}
    with open('user.txt') as f:
        for line in f:
            tmp = line.strip().split(':')
            if len(tmp) == 2:
                user_dict[tmp[0]] = tmp[1]
    if not name in user_dict:
        return "user not exist <a href='/'>返回</a>"
    user_dict.pop(name)
    user_list = []
    for user,pwd in user_dict.items():
        user_list.append(user+':'+pwd)
    with open('user.txt','w') as f:
        f.writelines('\n'.join(user_list))
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
    if name=='admin' and password=='admin':
        session['user']=name
    return redirect('/userlist')

# 用户退出
@app.route('/logout',methods=['get','post'])
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/useredit',methods=['get','post'])
def useredit():
    if 'user' not in session:
        return redirect('/login')
    name = request.args.get('user')
    return render_template('useredit.html',name=name)

@app.route('/usereditaction',methods=['get','post'])
def usereditaction():
    if 'user' not in session:
        return redirect('/login')
    # 防止不选择导致出错
    if not request.form.get('name'):
        return redirect('/userlist')
    name = request.form.get('name')
    password = request.form.get('password')
    user_dict = {}
    with open('user.txt') as f:
        for line in f:
            tmp = line.strip().split(':')
            if len(tmp) == 2:
                user_dict[tmp[0]] = tmp[1]
    if not name in user_dict:
        return "user not exist <a href='/'>返回</a>"
    user_dict[name] = password
    user_list = []
    for user,pwd in user_dict.items():
        user_list.append(user+':'+pwd)
    with open('user.txt','w') as f:
        f.writelines('\n'.join(user_list))
    return redirect('/userlist')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9093,debug=True)
