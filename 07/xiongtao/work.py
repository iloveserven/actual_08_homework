#coding: utf-8
from flask import Flask,render_template,request,redirect,session
import util

app = Flask(__name__)
app.secret_key = '/sad/abc@@123'

@app.route('/')
def index():
        return redirect('/show')

@app.route('/login_action',methods=['post'])
def login_action():
        user = request.form.get('name')
        passwd = request.form.get('passwd')
        if util.user_login(user,passwd)[0][0] == 0:
                return redirect('/login')
        else:
                session['user'] = user
                return redirect('/show')

@app.route('/user_add',methods=['post'])
def user_add():
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        util.user_add(user,passwd)
        return redirect('/show_user')

@app.route('/user_mod',methods=['post'])
def user_mod():
        id_num = request.form.get('id_num')
        passwd = request.form.get('passwd')
        util.user_mod(id_num,passwd)
        return redirect('/show_user')

@app.route('/user_del',methods=['post'])
def user_del():
        id_num = request.form.get('id_num')
        util.user_del(id_num)
        return redirect('/show_user')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/logout')
def logout():
        session.pop('user')
        return redirect('/login')

@app.route('/exec_file')
def exec_file():
        file_name = request.args.get('file_name')
        util.exe(file_name)
        return redirect('/show')

@app.route('/show')
def show():
        if not session.get('user',0):
                return redirect('/login')
        sort = request.args.get('sort')
        if sort == '0':
                return render_template('index.html',res_lst=util.info_show(),user=session['user'])
        else:
                return render_template('index.html',res_lst=util.info_show_sort(),user=session['user'])

@app.route('/show_user')
def show_user():
        if not session.get('user',0) or session.get('user',0) != 'admin':
                return redirect('/login')
        return render_template('user_show.html',res_lst=util.user_show())

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=10086,debug=True)
                                                     
