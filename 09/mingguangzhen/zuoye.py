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
    sql = 'select * from user'
    res = json.dumps(dbutil.user_info())
    # print res
    # res = ''
    # for line in dbutil.user_info():
    #     res += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % line
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
    cur_u = session.get('user', 'No')
    return render_template('log_page.html', logs=logs,page=page,all_pages=all_pages,page_list=page_list)

@app.route('/user_page')
def user_page():
    cur_u = session.get('user', 'None')
    user_info = dbutil.user_info()
    return render_template('user_page.html', user_info=user_info)

@app.route('/update_user')
def update_user():
    uppwd = request.args.get('uppwd')
    id = request.args.get('id')
    try:
        dbutil.update_user(uppwd,id)
    except:
        return 'error'
    else:
        return 'ok'

# @app.route('/update_user')
# def update_user():
#     uppwd = request.args.get('uppwd')
#     id = request.args.get('id')
#     dbutil.update_user(uppwd,id)
#     return redirect(url_for('user_page'))

@app.route('/add_user')
def add_user():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    sql = 'insert into user (username,password) values ("%s","%s")' % (user,pwd)
    try:
        dbutil.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'



# @app.route('/add_user', methods=['POST'])
# def add_user():
#     user = request.form.get('user')
#     pwd = request.form.get('pwd')
#     dbutil.ins_user(user=user,pwd=pwd)
#     return redirect(url_for('user_page'))
@app.route('/del_user')
def del_user():
    id = request.args.get('id')
    try:
        dbutil.del_user(id)
    except:
        return 'error'
    else:
        return 'ok'

# @app.route('/del_user')
# def del_user():
#     id = request.args.get('id')
#     dbutil.del_user(id)
#     return redirect(url_for('user_page'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    # print uinfo()
