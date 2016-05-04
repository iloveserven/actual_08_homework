#encoding=utf8
#
import MySQLdb as mysql

all_lines = 100
con = mysql.connect(db='mingguangzhen', host='180.153.191.128', user='reboot', passwd='reboot123')
con.autocommit(True)
cursor = con.cursor()
decide = cursor.execute('select * from log_data')
def insert_db():
    count_dict = {}
    cout = 0
    with open("E:\\Reboot\\Python01\\sublime_Text\\04\\www_access_20140823.log") as log_file:
        for line in log_file.readlines():
            temp = line.split()
            _tup = (temp[0], temp[8],)
            count_dict[_tup] = count_dict.get(_tup, 0) + 1
    rev_list = sorted(count_dict.items(), key = lambda x:x[1], reverse=True)[:all_lines]
    if decide < all_lines:
        for tup in rev_list:
            ins_sql = 'insert into log_data (ip,status,count) values("%s","%s","%s")' % (tup[0][0], tup[0][1], tup[1])
            cursor.execute(ins_sql)

def get_info(start,num):
    sql = 'select * from log_data limit %s,%s' % (start,num)
    cursor.execute(sql)
    return cursor.fetchall()

