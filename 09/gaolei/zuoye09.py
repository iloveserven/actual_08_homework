#-*- coding: utf-8 -*-
import logoper as log
from flask import Flask,render_template,request,redirect,session,json
app = Flask(__name__)
app.secret_key = 'sadfagraegrgaregareghhqare'
page = 0


@app.route('/login',methods=['GET','POST'])
def login():
    global page
    if 'user' in session:
        return redirect('/url')
    else:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            namelist = []
            name = request.form.get('user')
            pwd = request.form.get('passwd')
            sql = 'select username from user'
            log.sqloper(sql)
            for line in log.cursor.fetchall():
                namelist.append(line[0])
            if name in namelist:
                sql = 'select password from user where username="%s"' % name
                log.sqloper(sql)
                if pwd == log.cursor.fetchone()[0]:
                    session['user'] = name
                    page = 0
                    return redirect('/url')
                else:
                    return render_template('login.html',result='password error')
            else:
                return render_template('login.html',result='username not exist')



            


@app.route('/url')
def url():
    if 'user' in session:
        return render_template('url_sta.html')
    else:
        return redirect('/login')

@app.route('/user')
def user():
    if 'user' in session:
        return render_template('user_manage.html')
    else:
        return redirect('/login')
            

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


@app.route('/getsta')
def getsta():
    sql = 'select * from url_sta limit %d,20' % (page*20,)
    log.sqloper(sql)
    res = json.dumps(log.cursor.fetchall())
    return res

@app.route('/getpage')
def getpage():
    global page
    oper = request.args.get('oper')
    if oper == 'plus' and page < 4:
        page += 1
        return 'ok'
    elif oper == 'delete' and page > 0:
        page -= 1
        return 'ok'
    elif oper == 'turnto':
        page = int(request.args.get('page'))
        return 'ok'
    else:
        return 'error'

@app.route('/getuser')
def getuser():
    sql = 'select * from user'
    log.sqloper(sql)
    res = json.dumps(log.cursor.fetchall())
    return res

@app.route('/adduser')
def adduser():
    user = request.args.get('user')
    passwd = request.args.get('passwd')
    sql = 'insert into user(username,password) values("%s","%s")' % (user,passwd)
    try:
        log.sqloper(sql)
        log.sqloper('commit')
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/deluser')
def deluser():
    id = request.args.get('id')
    sql = 'delete from user where id=%s' % id
    try:
        log.sqloper(sql)
    except:
        return 'error'
    else:
        return 'ok'


if __name__ == '__main__':

    app.run(host = '0.0.0.0',port = 9023,debug = True)



