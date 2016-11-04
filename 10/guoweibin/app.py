#-*-coding:utf-8-*-
from flask import Flask, render_template,request,redirect,session
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import dbutil
import config

app=Flask(__name__)


db=dbutil.DB(config.db,config.db_host,config.db_user,config.db_passwd)

app.secret_key='asjkdhk123908789123-0329-kladjklklj??=-123'






@app.route('/testdata')
def  testdata():
        return 'ok'



@app.route('/login',methods=['get','post'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    elif request.method=='POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user=='admin' and pwd=='admin':
            session['user']='admin'
            return redirect('/')
        else:
            sql = 'select * from user where username="%s" and password="%s"'%(user,pwd)
            res = db.execute(sql)
            if len(res)>0:
                session['user'] = user
                # return  render_template('comuser.html')
                return redirect('/log')
            else:
                return 'not allowed'


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html',user=session['user'])
    else:
        return redirect('/login')

@app.route('/')
def index():
    sql='select * from user'
    print request.args
    if  request.args.get('order')=='desc':
        sql+='  order  by id desc'
    res=db.execute(sql)
    return render_template('index.html',userlist=res)

@app.route('/gettable')
def  gettable():
    sql="select  * from user  order by id"
    res = json.dumps(db.execute(sql))
    print res 
    return res


# @app.route('/usershow')
# def  usershow():
#     sql='select * from user'
#     print request.args
#     res=db.execute(sql)
#     return render_template('user.html',userlist=res)


@app.route('/adduser',methods=['POST'])
def adduser():
    user=request.form.get('user')
    pwd = request.form.get('pwd')

    sql='insert into user (username,password) values ("%s","%s")' %(user,pwd)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/deluser',methods=['POST'])
def deluser():
    id = request.form.get('id')
    sql= 'delete from user where id=%s' %(id)
    db.execute(sql)
    sender = '751629731@qq.com'
    receivers = ['gwbin1988@163.com'] 
    message= MIMEText('deleted user #'+id, 'plain')
    print message
    message['From'] = Header("reboot", 'utf-8')
    message['To'] =  Header("gwbin", 'utf-8')
    subject = 'Python 测试'
    message['Subject'] = Header(subject, 'utf-8')
    try:
          smtpObj = smtplib.SMTP('localhost')
          smtpObj.sendmail(sender, receivers, message.as_string())
          print "邮件发送成功"
    except smtplib.SMTPException:
         print "Error: 无法发送邮件"

    return 'ok'

@app.route('/updateuser',methods=['POST'])
def updateuser():
    id=request.form.get('id')
    pwd = request.form.get('pwd')
    sql = 'update user set password="%s" where id=%s'%(pwd,id)
    db.execute(sql)
    return 'ok'

@app.route('/machine')
def machine():
        sql="select  * from machine"
        # res=dbutil.execute(sql)
        # print res
        # return "ok"
        res=db.execute(sql)
        return render_template('machine.html',Hostlist=res)

@app.route('/gethostlist')
def gethostlist():
    sql='select * from machine'
    res=json.dumps(db.execute(sql))
    print res
    return res 

@app.route('/addHost',methods=['POST'])
def addHost():
    Hostname=request.form.get('Hostname')
    Hostsize=request.form.get('Hostsize')
    HostDate=request.form.get('HostDate')
    Email=request.form.get('Email')

    sql="insert into machine(Hostname,Hostsize,HostDate,Email) values('%s','%s','%s','%s')"%(Hostname,Hostsize,HostDate,Email)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'


@app.route('/delHost',methods=['POST'])
def delHost():
        id = request.form.get('id')
        sql='delete from machine where Hostid=%s' %(id)
        db.execute(sql)
        return 'ok'

@app.route('/updateHost',methods=['POST'])
def  updateHost():
    Hostid=request.form.get('Hostid')
    Hostname=request.form.get('Hostname')
    Hostsize=request.form.get('Hostsize')
    HostDate=request.form.get('HostDate')
    Email=request.form.get('Email')
    sql = 'update machine  set Hostname="%s" ,Hostsize="%s",HostDate="%s",Email="%s" where Hostid=%s'%(Hostname,Hostsize,HostDate,Email,Hostid)
    db.execute(sql)
    return 'ok'






   
 



@app.route('/log')
def log():
    if  'user'  in session:
            # page=int(request.args.get('page',1))
            # num=5
            # dbutil.execute("select  count(*)  from  log")
            # total=dbutil.fetchone()[0]
            # print total
            # if  total%num==0:
            #             pages=total/num
            # else:
            #              pages=total/num+1
            # start_position=(page-1)*num
            # dbutil.execute('select * from logdb limit  %s, %s '%(start_position,num))
            # data=dbutil.fetchall()
            # print data
            # return render_template('loglist.html',log_list=data,pages=pages,user=session['user'])

            page = int(request.args.get('page',0))
            count=request.args.get('count',10)
            sql='select *  from log limit %s ,%s'%(int(page)*int(count),count)
            res = db.execute(sql)
            return render_template('log.html',logs=res,page=page,user=session['user'])
    else:
        return redirect('/login')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9099,debug=True)



