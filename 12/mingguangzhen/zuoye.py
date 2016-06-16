#encoding=utf-8
#
from flask import Flask,render_template,redirect,url_for,session,request
import dbutil
import json
import sys
import config
import tools

reload(sys)
sys.setdefaultencoding('utf-8')
db = dbutil.DB(db=config.db,host=config.db_host,user=config.db_user,passwd=config.db_passwd)
app = Flask(__name__)
app.secret_key = tools.random_str(100)

@app.route('/testdata')
def testdata():
    return 'hello ajax'

@app.route('/uinfo')
def uinfo():
    sql = 'select id,username,password from user'
    res = json.dumps(db.execute(sql))
    return res

@app.route('/resinfo')
def resinfo():
    sql = 'select * from res_mgt'
    res = json.dumps(db.execute(sql))
    return res


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    info_dict = {}
    sql = 'select username,password from user'
    res_list = db.execute(sql)
    for tup in res_list:
        info_dict[tup[0]] = tup[1]

    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user not in info_dict:
            return 'user not exists.'
        elif info_dict[user] == pwd:
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
    sql = 'select * from log_data limit %s,%s' % ((page-1)*cont,cont)
    logs = db.execute(sql)

    return render_template('log_page.html', logs=logs,page=page,all_pages=all_pages,page_list=page_list)

@app.route('/user_page')
def user_page():
    return render_template('user_page.html')

@app.route('/update_user', methods=['POST'])
def update_user():
    uppwd = request.form.get('uppwd')
    id = request.form.get('id')
    sql = 'update user set password="%s" where id=%s' % (uppwd,id)

    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print user, pwd
    sql = 'insert into user (username,password) values ("%s","%s")' % (user,pwd)
    if user:
        try:
            db.execute(sql)
        except:
            return 'error'
        else:
            return 'ok'
    else:
        return 'error'


@app.route('/del_user', methods=['POST'])
def del_user():

    id = request.form.get('id',None)
    sql = 'delete from user where id=%s' % (id)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/res_mgt')
def res_mgt():
    return render_template('res_mgt.html')

@app.route('/add_res', methods=['POST'])
def add_res():
    host_name = request.form.get('host_name',None)
    cpu_core = request.form.get('cpu_core',None)
    mem_size = request.form.get('mem_size',None)
    val_per = request.form.get('val_per',None)
    contacts = request.form.get('contacts',None)
    sql = 'insert into res_mgt(host_name,cpu_core,mem_size,val_per,contacts) values("%s","%s","%s","%s","%s")' % (host_name,cpu_core,mem_size,val_per,contacts)

    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/del_res', methods=['POST'])
def del_res():
    id = request.form.get('id')
    sql = 'delete from res_mgt where id=%s' % (id)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/update_res', methods=['POST'])
def update_res():
    userid = request.form.get('userid',None)
    host_name = request.form.get('host_name',None)
    cpu_core = request.form.get('cpu_core',None)
    mem_size = request.form.get('mem_size',None)
    val_per = request.form.get('val_per',None)
    contacts = request.form.get('contacts',None)
    print userid,host_name,cpu_core,mem_size,val_per,contacts

    sql = 'update res_mgt set host_name="%s",cpu_core="%s",mem_size="%s",val_per="%s",contacts="%s" where id=%s' % (host_name, cpu_core, mem_size, val_per, contacts, userid)
    try:
        db.execute(sql) 
    except:
        return 'error'
    else:
        return 'ok'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
@app.route('/httpcount')
def httpcount():
    sql = 'select * from log_data'
    log_data = db.execute(sql)
    log_handle = {}
    res = {'legend_data':[],'series_data':[]}
    for bar in log_data:
        log_handle[bar[2]] = log_handle.get(bar[2],0) + int(bar[3])
    for key,val in log_handle.items():
        res['legend_data'].append(key)
        res['series_data'].append({'value':val,'name':key})
    # print res
    return json.dumps(res)

@app.route('/log_pie')
def log_pie():
    return render_template('log_pie.html')

@app.route('/httpscatter')
def httpscatter():
    sql = 'select ip,status,geox,geoy,count from ipmap order by id'
    log_data = db.execute(sql)
    res = {'data':[],'max_val':1000,'min_val':0}
    for bar in log_data:
        res['data'].append({'name':bar[0],'value':[bar[2],bar[3],bar[4]]})
    return json.dumps(res)

@app.route('/log_scatter')
def log_scatter():
    return render_template('log_scatter.html')

@app.route('/httpmap')
def httpmap():
    res = {'ipgeo':{}, 'normal':[], 'failed':[], 'keep':[]}
    sql = 'select ip,status,geox,geoy,count from ipmap order by id'
    log_data = db.execute(sql)
    res['ipgeo']['200'] = ['116.4551','40.2539']
    res['ipgeo']['404'] = ['121.4648','31.2891']
    res['ipgeo']['304'] = ['113.5107','23.2196']
    for bar in log_data:
        if int(bar[4]) > 200:
            continue
        res['ipgeo'][bar[0]] = [bar[2],bar[3]]
        if bar[1] == '200':
            res['normal'].append([{'name':bar[1]},{'name':bar[0],'value':bar[4]}])
        elif bar[1] == '404':
            res['failed'].append([{'name':bar[1]},{'name':bar[0],'value':bar[4]}])
        elif bar[1] == '304':
            res['keep'].append([{'name':bar[1]},{'name':bar[0],'value':bar[4]}])
    return json.dumps(res)



@app.route('/log_map')
def log_map():
    return render_template('log_map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=True)
