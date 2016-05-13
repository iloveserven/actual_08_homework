#import MySQLdb as mysql
from flask import Flask, render_template,request,redirect,session
app=Flask(__name__)
#con = mysql.connect(db='woniu8',host='localhost',user='reboot',passwd='reboot123')
#con.autocommit(True)
#cursor = con.cursor()
import dbutil

app.secret_key='asjkdhk123908789123-0329-kladjklklj??=-123'


@app.route('/testpage')
def  testpage():
    return render_template('testpage.html')


@app.route('/login',methods=['get','post'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    elif request.method=='POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user=='admin' and pwd=='admin':
            session['user']='admin'
            return redirect('/usershow')
        else:
            sql = 'select * from user where username="%s" and password="%s"'%(user,pwd)
            res = dbutil.execute(sql)
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

# @app.route('/home')
# def home():
#     if 'user' in session:
#         return render_template('home.html',user=session['user'])
#     else:
#         return redirect('/login')

@app.route('/')
def index():
       if 'user' in session:
                         return render_template('index.html',user=session['user'])
       else:
                        return redirect('/login')

@app.route('/usershow')
def  usershow():
    sql='select * from user'
    print request.args
    res=dbutil.execute(sql)
    return render_template('user.html',userlist=res)

    # sql = 'select * from user'
    # # print request.args
    # # if request.args.get('order')=='desc':
    # #     sql+=' order by id desc'
    # res = dbutil.execute(sql)
    # return render_template('index.html',userlist=res)

@app.route('/adduser',methods=['POST'])
def adduser():
    user=request.form.get('user')
    pwd = request.form.get('pwd')

    sql='insert into user (username,password) values ("%s","%s")' %(user,pwd)
    try:
        dbutil.execute(sql)
    except:
        return 'error'
    else:
        return redirect('usershow')

@app.route('/deluser')
def deluser():
    id = request.args.get('id')
    sql= 'delete from user where id=%s' %(id)
    dbutil.execute(sql)
    return redirect('usershow')

@app.route('/updateuser')
def updateuser():
    id=request.args.get('id')
    pwd = request.args.get('pwd')
    sql = 'update user set password="%s" where id=%s'%(pwd,id)
    dbutil.execute(sql)
    return redirect('usershow')


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
            res = dbutil.execute(sql)
            return render_template('log.html',logs=res,page=page,user=session['user'])
    else:
        return redirect('/login')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9099,debug=True)



