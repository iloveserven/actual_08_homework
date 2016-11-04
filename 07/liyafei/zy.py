#!/usr/bin/python
# coding=utf-8
import MySQLdb as mysql
from flask import Flask,render_template,request,redirect,session
import logfile,sql
app=Flask(__name__)
app.secret_key='adsfasdf90239rkdsakKSDANFOAKDNFKADSNFKASDFNKADFKLDASLFK'

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
        userinfo = sql.select_u(user)
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
        logfile.data_file()
        s_list = sql.select_d()
        name=session['user']
        return render_template('data.html',userlist=s_list,name=name)
    else:
        return redirect('/')
@app.route('/userlist')
def userlist():
    if 'user' in session and session['user'] == 'admin':
        u_list = sql.select_u_all()
        return render_template('userlist.html',userlist=u_list)  
    else:
        return redirect('/')

@app.route('/adduser',methods=['post'])
def adduser():
    try:
        user= request.form.get('user')
        pwd = request.form.get('pwd')
        user = user.strip()
        pwd = pwd.strip()
        sql.insert_u(user,pwd)   
        return redirect('/userlist') 
    except:
        return "添加失败,请检查！"
@app.route('/update')
def updateuser():
    try:
        idnum =  request.args.get('id')
        pwd =  request.args.get('pwd')
        pwd = pwd.strip()
        sql.update_u(pwd,idnum)
        return redirect('/userlist')
    except:
        return "修改失败,请检查！"
@app.route('/deluser')
def deluser():
    try:
        idnum =  request.args.get('id')
        tmp=sql.user_id(idnum)
        user_id =tmp[0][0]
        if user_id.strip() == 'admin':
            return "Sorry ,此用户不能删除，请返回!"
        else:
            sql.del_u(idnum)
            return redirect('/userlist')
    except:
        return "删除用户失败，请检查！"
@app.route('/datauser')
def datauser():
    if 'user' in session and session['user'] != 'admin':
        logfile.data_file()
        s_list = sql.select_d()
        name=session['user']
        return render_template('user.html',userlist=s_list,name=name)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

