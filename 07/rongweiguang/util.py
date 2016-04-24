#!/usr/bin/python
import MySQLdb as mysql

def info_show():
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute('select * from log order by count')
	return cursor.fetchall()

def info_show_sort():
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute("select * from log order by count desc")
	return cursor.fetchall()

def user_show():
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute('select * from user')
	return cursor.fetchall()

def user_add(user,passwd):
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute("insert into user (username,password) values('%s',password('%s'))"%(user,passwd))
	con.commit()

def user_del(id_num):
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute("delete from user where id='%s'"%(id_num))
	con.commit()

def user_mod(id_num,passwd):
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute("update user set password=password('%s') where id='%s'"%(passwd,id_num))
	con.commit()

def user_login(user,passwd):
	con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
	cursor = con.cursor()
	cursor.execute("select count(*) from user where username='%s' and password=password('%s')"%(user,passwd))
	return cursor.fetchall()

def exe(file_name):
        with open(file_name) as f:
                tmp_dict = {}
                res_dict = {}
                tmp_lst = []
                for line in f:
                        tmp = line.split(' ')
                        tmp_str = tmp[0]+' '+tmp[8]
                        tmp_dict[tmp_str] = tmp_dict.get(tmp_str,0)+1
        reverse_dict = {}
        for k,v in tmp_dict.items():
                reverse_dict.setdefault(v,[]).append(k)

        v_list = reverse_dict.keys()

        con = mysql.connect(db='test',host='localhost',user='root',passwd='123456')
        cursor = con.cursor()
        cursor.execute("delete from log")
        sql = "insert into log (ip,status,count) values('%s','%s','%s')"

        count = 0
        while count<100:
                max_val = max(v_list)
                v_list.remove(max_val)
                for info in reverse_dict[max_val]:
                        cursor.execute(sql%(info.split(' ')[0],info.split(' ')[1],max_val))
                        count += 1
                        if count == 100:
                                break
        con.commit()
