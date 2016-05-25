#encoding=utf8
#
import MySQLdb as mysql
con = mysql.connect(db='mingguangzhen', host='180.153.191.128', user='reboot', passwd='reboot123')
con.autocommit(True)
cursor = con.cursor()

def get_info():
    sql = 'select id,username,password from user'
    cursor.execute(sql)
    res_list = cursor.fetchall()
    return res_list

def auth_info():
    info_dict = {}
    sql = 'select username,password from user'
    cursor.execute(sql)
    res_list = cursor.fetchall()
    for tup in res_list:
        info_dict[tup[0]] = tup[1]
    return info_dict

def ins_user(user,pwd):
    sql = 'insert into user(username,password) values("%s","%s")' % (user,pwd)
    cursor.execute(sql)
    return True

def del_user(id):
    sql = 'delete from user where id=%s' % (id)
    cursor.execute(sql)
    return True

def update_user(uppwd,id):
    sql = 'update user set password="%s" where id=%s' % (uppwd,id)
    cursor.execute(sql)
    return True

#print get_info()
