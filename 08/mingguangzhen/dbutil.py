#encoding=utf-8

import MySQLdb as mysql

con = None
cursor = None
def connect():
    global con 
    global cursor
    con = mysql.connect(db='mingguangzhen', host='180.153.191.128', user='reboot', passwd='reboot123')
    con.autocommit(True)
    cursor = con.cursor()

def execute(sql):
    try:
        cursor.execute(sql)
    except Exception, err:
        #print err
        try:
            cursor.close()
            con.close()
        except Exception as e:
            pass
        print 'con db again.'
        connect()
        cursor.execute(sql)
    return cursor.fetchall()

def log_info(start,cont):
    sql = 'select * from log_data limit %s,%s' % (start,cont)
    return execute(sql)




'''
For user management.
Support add/del/modified/select
'''

def user_info():
    sql = 'select id,username,password from user'
    return execute(sql)

def auth_info():
    info_dict = {}
    sql = 'select username,password from user'
    res_list = execute(sql)
    for tup in res_list:
        info_dict[tup[0]] = tup[1]
    return info_dict

def ins_user(user,pwd):
    sql = 'insert into user(username,password) values("%s","%s")' % (user,pwd)
    execute(sql)
    return True

def del_user(id):
    sql = 'delete from user where id=%s' % (id)
    execute(sql)
    return True

def update_user(uppwd,id):
    sql = 'update user set password="%s" where id=%s' % (uppwd,id)
    execute(sql)
    return True