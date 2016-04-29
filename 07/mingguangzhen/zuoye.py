#encoding=utf8

from flask import Flask,render_template,request,redirect,session
import get_data, get_user

app = Flask(__name__)
app.secret_key = '1234567890!@#$%^&*()'
decide_boo = True

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/activelogin', methods=['POST'])
def activelogin():
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user not in get_user.get_info():
        return 'user not exists.'
    elif get_user.get_info()[user] == pwd:
        session['user'] = user
        session['init'] = 0
        session['m_page'] = 1
        return redirect('/data_count')
    else:
        return 'password error.'

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('init', None)
    session.pop('m_page', None)
    return redirect('/')

@app.route('/data_count')
def log_count():
    if 'user' not in session:
        return redirect('/')
    count = 8
    sql = 'select * from log_data limit %s,%s' % (session['init'],count)
    data_list = get_data.get_info(sql)
    next_page = request.args.get('next', None)
    prev_page = request.args.get('previsous', None)
    session['page'] = request.args.get('page', 0)
    page = int(session['page'])
    all_page = 100 / count
    if 100 % count:
        all_page += 1

    if (page != 0) and (int(page) <= (all_page)):
        session['init'] = (page-1) * count
        sql = 'select * from log_data limit %s,%s' % (session['init'],count)
        data_list = get_data.get_info(sql)
        session['m_page'] = page
        return render_template('data_count.html', data_list=data_list, page=page,all_page=all_page, cur_user=session['user'])

    elif (next_page != None) and (session['init'] < (100 - count)):
        session['init'] += count
        session['m_page'] = int(session['m_page']) + 1
        sql = 'select * from log_data limit %s,%s' % (session['init'],count)
        data_list = get_data.get_info(sql)
        return render_template('data_count.html', data_list=data_list, page=session['m_page'], all_page=all_page, cur_user=session['user'])

    elif (prev_page != None) and (session['init'] > 0):
        session['init'] -= count
        session['m_page'] = int(session['m_page']) - 1
        sql = 'select * from log_data limit %s,%s' % (session['init'],count)
        data_list = get_data.get_info(sql)
        return render_template('data_count.html', data_list=data_list, page=session['m_page'], all_page=all_page, cur_user=session['user'])
    return render_template('data_count.html', data_list=data_list,page=session['m_page'], all_page=all_page, cur_user=session['user'])

@app.route('/user_management')
def user_management():
    if session['user'] != 'admin':
        return redirect('/data_count')
    user_dict = get_user.get_info()
    return render_template('user.html', user_dict=user_dict)

if __name__ == '__main__':
    if decide_boo == True:
        get_data.insert_db()
        decide_boo = False
    app.run(host='0.0.0.0', port=1234, debug=True)
