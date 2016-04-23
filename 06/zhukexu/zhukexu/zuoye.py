#!/usr/bin/env python

from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='ldakjflkadjfldkajgkdaljgadsjgadskg'

@app.route('/')
def index():
    if 'user' not in  session:
        return redirect('/login')
#    username = 'reboot'
#    return render_template('index.html',username=username)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'user' in  session:
        return redirect('/')
    return render_template('login.html')
#    session.pop('user')
#    return redirect('/login')

@app.route('/loginaction',methods=['post'])
def loginaction():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    if user=='admin' and passwd=='admin':
        session['user']='admin'
    return redirect('/data')

@app.route('/data')
def data():
    if 'user' not in session:
        return redirect('/login')
    userlist = []
    with open('/test/user.txt') as f:
        for line in f:
            tmp = line.split(':')
            if len(tmp)==2:
                userlist.append(tmp)
    return render_template('data.html',userlist=userlist)


@app.route('/deluser')
def deluser():
    user = request.args.get('user')
    if user in file_data:
        file_data.pop(user)
        update_data()
    return redirect('/')

file_data = {}
def update_data():
    with open('/test/user.txt') as f:
        for line in f:
            if not line:
                continue
            tmp = line.split(':')
            if len(tmp) == 2:
                file_data[tmp[0]]=tmp[1].replace('\n','')

def update_file():
    user_list=[]
    for k.v in file_data.items():
        user_list.append('%s:%s'%(k,v))
    with open('/test/user.txt','w') as f:
        f.write('\n'.join(user_list))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)


