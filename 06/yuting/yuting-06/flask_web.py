#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = '123dansoiyda97tq8ev1jbedIASDA7RXF12BD8A9ZY9gTS8ASHDOASHC98'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
    username =  request.form.get('username')
    password =  request.form.get('password')
    if username == 'admin' and password == 'admin123':
        session['sid'] = 'admin_user_id'
    return redirect('/passwd')    

@app.route('/')
def index():
    # return 'Hello flask'
    userList = []
    with open('passwd.txt','r') as f:
        for line in f:
            tmp = line.split(':')
            if len(tmp) == 2:
                userList.append(tmp)
    username = 'admin'
    return render_template('index.html',username=username,userList=userList)

@app.route('/data')
def data():
    name =  request.args.get('name')
    age =  request.args.get('age')
    return 'Hello name:%s,age%s'%(name,age)

@app.route('/test/<username>')
def test(username):
    return 'Hello name:%s'%(username)

# @app.route('/passwd')
# def pwd():
#     if 'sid' not in session:
#         return redirect('/login')
#     else:
#         html = """<table border="1">
#               <tr><td>name</td><td>password</td></tr>
#               """
#         with open('passwd.txt','r') as f:
#             for item in f:
#                 if len(item) > 2:
#                     name = item.split(':')[0]
#                     passwd = item.split(':')[1]
#                     html += "<tr><td>%s</td><td>%s</td></tr>"%(name,passwd) + "\n"
#         html += "</table>"
#         return html

@app.route('/adduser',methods=['post'])
def adduser():
    if 'sid' not in session:
        return redirect('/login')
    else:
        # print request
        # print request.args
        # username =  request.args.get('username')
        # password =  request.args.get('password')
        username =  request.form.get('username')
        password =  request.form.get('password')
        with open('passwd.txt','a') as f:
            item = '\n' + username + ':' + password
            f.writelines(item)
        return redirect('showUser')

@app.route('/deluser',methods=['post'])
def delUser():
    if 'sid' not in session:
        return redirect('/login')
    else:
        username =  request.form.get('username')
        userList = []
        userFound = False
        with open('passwd.txt','r') as f:
            for line in f:
                tmp = line.split(':')
                if username == tmp[0]:
                    userFound = True
                else:
                    userList.append(line)
        if True == userFound:
            with open('passwd.txt','w') as f:
                for item in userList:
                    f.writelines(item)
        return render_template('delResult.html',userFound=userFound,username=username)

@app.route('/showUser')
def showUser():
    if 'sid' not in session:
        return redirect('/login')
    else:
        userList = []
        with open('passwd.txt','r') as f:
            for line in f:
                tmp = line.split(':')
                if len(tmp) == 2:
                    userList.append(tmp)
        return render_template('showUser.html',userList=userList)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9093,debug=True)