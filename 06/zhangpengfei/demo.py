#coding:utf-8
#
# import reboot
# reboot.hello()

from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='sdqnjweh28ujsdauehu82da2'


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    if user == 'admin' and passwd == 'admin':
        session['user'] = 'admin'
    return redirect('/data')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')



@app.route('/adduser',methods=['post'])
def adduser():
    user = request.form.get('user')
    password = request.form.get('password')
    with open('user.txt','a') as f:
        f.write('\n'+user+':'+password)
    # return 'OK'
    return  redirect('/data')

@app.route('/deluser',methods=['post'])
def deluser():
    flag = False
    user = request.form.get('user')
    arr = []
    with open('user.txt','r') as f:
        for line in f:
            if line.replace('\n','') == user:
                flag = True
            else:
                arr.append(line.replace('\n',''))
    with open('user.txt','w') as f:
        count  = 0
        for line in arr:
            if count == 0:
                f.write(line)
                count = 1
            else:
                f.write('\n')
                f.write(line)
    return redirect('/data')



@app.route('/data')
def data():
    if 'user' not in  session:
        return redirect('/login')
    userlist = []
    with open('user.txt') as f:
        for line in f:
            tmp = line.split(':')
            if len(tmp) == 2:
                userlist.append(tmp)
    return render_template('data.html',userlist=userlist)





@app.route('/name')
def name():
    try:
        user= request.args.get('user')
        with open('user.txt') as f:
            for i in f.readlines():
                s = i.split(':')
                if s[0] == user:
                    passwd = s[1]
        return '%s %s'  % (user,passwd)
    except:
        return 'nothing'



@app.route('/hehe')
def hehe():
    name = request.args.get('name')
    age = request.args.get('age')
    print name
    print age
    return  'hello %s %s ' %(name ,age)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)