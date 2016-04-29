#encoding=utf8
#
import MySQLdb as mysql
con = mysql.connect(db='mingguangzhen', host='180.153.191.128', user='reboot', passwd='reboot123')
con.autocommit(True)
cursor = con.cursor()

def get_info():
    info_dict = {}
    sql = 'select username,password from user'
    cursor.execute(sql)
    res_list = cursor.fetchall()
    for tup in res_list:
        info_dict[tup[0]] = tup[1]
    return info_dict
#print get_info()
