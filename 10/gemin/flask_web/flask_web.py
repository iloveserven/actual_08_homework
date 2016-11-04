from flask import Flask,request,render_template,redirect,session
import dbutil
import json
import datetime
app = Flask(__name__)

app.secret_key = 'adfadfdfadfasf'

@app.route('/testdata')
def testdata():
    return 'hello flask'

@app.route('/gettable')
def gettable():
    sql = 'select * from user'
    # res = ''
    # for line in dbutil.execute_sql(sql):
    #     res += '<tr><td>%s</td><td>%s</td><td>%s</td>'%(line[0],line[1],line[2])
    res = json.dumps(dbutil.execute_sql(sql))
    return res

@app.route('/getasset')
def getasset():
    sql = 'select * from asset'
    # res = ''
    # for line in dbutil.execute_sql(sql):
    #     res += '<tr><td>%s</td><td>%s</td><td>%s</td>'%(line[0],line[1],line[2])
    tmp = dbutil.execute_sql(sql)
    res = json.dumps(tmp)
    return res

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username','')
        password = request.form.get('password','')
        if username == 'admin' and password == 'admin':
            session['username'] = 'admin'
            return redirect('/user')
        else:
            sql = 'select * from user where username="%s" and password="%s"'%(username,password)
            res = dbutil.execute_sql(sql)
            if len(res)>0:
                session['username'] = username
                return redirect('/user')
            else:
                return 'No Permission'

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html',user=session['username'])
    else:
        return 'Not Allowed'

@app.route('/user')
def user():
    sql = 'select * from user'
    if request.args.get('order') == 'desc':
        sql += ' order by id desc'
    elif request.args.get('order') == '':
        sql += ' order by id'
    res = dbutil.execute_sql(sql)
    return render_template('user.html',userlist=res)

@app.route('/adduser',methods=["POST","GET"])
def adduser():
    username = request.args.get('username','')
    password = request.args.get('password','')
    sql = 'insert into user (username,password) values("%s","%s")'%(username,password)
    try:
        dbutil.execute_sql(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/deluser')
def deluser():
    id = request.args.get('id')
    sql = 'delete from user where id = %s'%(id,)
    dbutil.execute_sql(sql)
    return 'ok'

@app.route('/updateuser')
def updateuser():
    id = request.args.get('id')
    password = request.args.get('password')
    sql = 'update user set password = "%s" where id = %s'%(password,id)
    dbutil.execute_sql(sql)
    return 'ok'

@app.route('/log')
def log():
    sql = 'select * from log'
    if request.args.get('order') == 'desc':
        sql += ' order by id desc'
    elif request.args.get('order') == '':
        sql += ' order by id'
    page = int(request.args.get('page',0))
    count = request.args.get('count',10)
    # sql = 'select * from log limit %s,%s'%(int(page)*int(count),count)
    sql += ' limit %s,%s'%(int(page)*int(count),count)
    res = dbutil.execute_sql(sql)
    return render_template('log.html',logs=res,page=page)

@app.route('/test')
def lay():
    return render_template('test.html')

@app.route('/asset')
def asset():
    return render_template('asset.html')

@app.route('/addasset')
def addasset():
    hostname = request.args.get('hostname','')
    memory = request.args.get('memory','')
    expiretime = request.args.get('expiretime','')
    chargemail = request.args.get('chargemail','')
    sql = 'insert into asset(hostname,memory,expiretime,chargemail) values("%s","%s","%s","%s")' % (hostname,memory,expiretime,chargemail)
    print sql
    try:
        dbutil.execute_sql(sql)
    except Exception as e:
        return  str(e)
    else:
        return 'ok'

@app.route('/delasset')
def delasset():
    id = request.args.get('id')
    sql = 'delete from asset where id = %s' % (id,)
    dbutil.execute_sql(sql)
    return 'ok'

@app.route('/updateasset')
def updateasset():
    id = request.args.get('id')
    hostname = request.args.get('hostname')
    memory = request.args.get('memory')
    sql = 'update asset set hostname = "%s",memory = "%s" where id = %s'%(hostname,memory,id)
    dbutil.execute_sql(sql)
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)