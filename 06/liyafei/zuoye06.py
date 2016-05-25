#!/usr/bin/python
# coding=utf-8
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='adsfasdf90239rkdsakKSDANFOAKDNFKADSNFKASDFNKADFKLDASLFK'

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/data')
    return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    if user.strip() == 'admin' and passwd.strip()=='admin':
        session['user'] = 'admin'
        return redirect('/data')
    else:
        #return 'fuck you,get out!'
        return render_template('error.html')
@app.route('/loginout')
def loginout():
    session.pop('user')
    return redirect('/') 

@app.route('/data')
def data():
    if 'user' not in session:
        return redirect('/')
    userlist = []
    with open('pass.txt') as f:
        for line in f.readlines():
            lst = line.split(':')
            if len(lst) == 2:
                userlist.append(lst)
    return render_template('data.html',userlist=userlist)

@app.route('/adduser',methods=['post'])
def adduser():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    if user.strip() != '' and passwd.strip() != '': 
        with open('pass.txt','a') as f:
            f.write(user+':'+passwd+'\n')
    return redirect('/data')
@app.route('/deluser',methods=['post'])
def deluser():
    user = request.form.get('user')
    if user:
        with open('pass.txt','r') as f:
            arr = f.readlines()
        with open('pass.txt','w') as file_:
            for line in arr:
                line_ = line.split()
                user_ = user.split()
                if  line_ == user_:
                    continue
                else:
                    file_.write(line)
        return redirect('/data')
    return "请选择删除的值!!"
if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
