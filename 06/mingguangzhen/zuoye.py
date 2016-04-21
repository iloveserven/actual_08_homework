#encoding=utf8

from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key='2992kshdkfsdj'

def handle():
    user_dict = {}
    with open('user.txt') as f:
        for line in f:
            tmp = line.split(':')
            if len(tmp) == 2:
                user_dict[tmp[0]] = tmp[1].split('\n')[0]
    return user_dict

@app.route('/')
def index():
    return 'hello world'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_auth', methods=['post'])
def login_auth():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    if (user in handle()) and (handle()[user] == passwd):
        session['user'] = (user,passwd)
        if user == 'admin':
            return redirect('/info')
        else:
            return render_template('permission.html')
    else:
        return redirect('/login')
@app.route('/modify')
def modify():
    add_user = request.args.get('add_user')
    add_passwd = request.args.get('add_passwd')
    status = request.args.get('res')
    tmp_dict = handle().copy()
    if status == 'Add':
        if add_user in handle():
            return 'User already exists.'
        else:
            with open('user.txt', 'a') as f:
                f.write('\n'+add_user+':'+add_passwd)
        tmp_dict = handle().copy()

    elif status == 'Del':
        if add_user in handle():
            with open('user.txt', 'w+') as f:
                for key,val in tmp_dict.items():
                    if key != add_user:
                        f.write('\n'+key+':'+val)
        else:
            return 'User not exists.'
    return redirect('/info')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')
@app.route('/info')
def info():
    return render_template('info.html', _dict=handle())


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9905,debug=True)


