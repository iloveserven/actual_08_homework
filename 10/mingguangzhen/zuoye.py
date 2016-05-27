#encoding=utf-8
#
from flask import Flask,render_template,redirect,url_for,session,request
import dbutil
import json

app = Flask(__name__)
app.secret_key = '1234567890!@#$%^&*()'

@app.route('/testdata')
def testdata():
    return 'hello ajax'

@app.route('/uinfo')
def uinfo():
    # sql = 'select * from user'
    res = json.dumps(dbutil.user_info())
    return res

@app.route('/resinfo')
def resinfo():
    # sql = 'select * from res_mgt'
    res = json.dumps(dbutil.res_info())
    return res


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user not in dbutil.auth_info():
            return 'user not exists.'
        elif dbutil.auth_info()[user] == pwd:
            session['user'] = user
            return redirect(url_for('user_page'))
        else:
            return 'password error.'

@app.route('/log_page')
def log_page():
    page = request.args.get('page',1)
    cont = request.args.get('cont',10)
    page = int(page)
    cont = int(cont)
    if 100%cont:
        all_pages = (100/cont) + 1
    else:
        all_pages = 100/cont
    page_list = range(all_pages)
    logs = dbutil.log_info((page-1)*cont,cont)
    return render_template('log_page.html', logs=logs,page=page,all_pages=all_pages,page_list=page_list)

@app.route('/user_page')
def user_page():
    return render_template('user_page.html')

@app.route('/update_user')
def update_user():
    uppwd = request.args.get('uppwd')
    id = request.args.get('id')
    # print uppwd, id
    try:
        dbutil.update_user(uppwd,id)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/add_user')
def add_user():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    sql = 'insert into user (username,password) values ("%s","%s")' % (user,pwd)
    if user:
        try:
            dbutil.execute(sql)
        except:
            return 'error'
        else:
            return 'ok'
    else:
        return 'error'


@app.route('/del_user')
def del_user():
    id = request.args.get('id',None)
    try:
        dbutil.del_user(id)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/res_mgt')
def res_mgt():
    return render_template('res_mgt.html')

@app.route('/add_res')
def add_res():
    host_name = request.args.get('host_name',None)
    cpu_core = request.args.get('cpu_core',None)
    mem_size = request.args.get('mem_size',None)
    val_per = request.args.get('val_per',None)
    contacts = request.args.get('contacts',None)
    print host_name,cpu_core,mem_size,val_per,contacts
    try:
        dbutil.ins_res(host_name,cpu_core,mem_size,val_per,contacts)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/del_res')
def del_res():
    id = request.args.get('id')
    try:
        dbutil.del_res(id)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/update_res')
def update_res():
    userid = request.args.get('userid')
    host_name = request.args.get('host_name')
    cpu_core = request.args.get('cpu_core')
    mem_size = request.args.get('mem_size')
    val_per = request.args.get('val_per')
    contacts = request.args.get('contacts')
    res_dict = {'userid':userid,
                'host_name':host_name,
                'cpu_core':cpu_core,
                'mem_size':mem_size,
                'val_per':val_per,
                'contacts':contacts}
    try:
        dbutil.update_res(res_dict)
    except:
        return 'error'
    else:
        return 'ok'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
