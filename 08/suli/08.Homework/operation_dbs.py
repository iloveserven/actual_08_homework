#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Other: suli
# Time: 2016.04.25 14:30
#
# 读取数据库

import MySQLdb as mysql

host = ""
port = 0
user = ""
pwd = ""
db = 'day7'

# 从配置文件中读取连接数据库的各项参数
fa = open("init.config", "rb+")
tmp = fa.read()
fa.close()
if tmp != "":
    tmp = tmp.split("\n")
    host = tmp[0]
    port = int(tmp[1])
    user = tmp[2]
    pwd = tmp[3]
del tmp


# 初始化连接数据库各项参数,并写入配置文件
def init_var(HOST, PORT, USER, PWD):
    global host
    global port
    global user
    global pwd
    host = HOST
    port = PORT
    user = USER
    pwd = PWD
    tmp = "%s\n%s\n%s\n%s" % (HOST, PORT, USER, PWD)
    # print tmp
    f = open("init.config", "wb")
    f.write(tmp)
    f.close()
    del tmp


# 开始连接
def get_conn():
    conn = mysql.connect(host=host, port=port, user=user, passwd=pwd, db=db)
    return conn


# 执行任何sql 错误返回1
def execute_mysql(sql, debug=False):
    if debug:
        print "[SQL: %s]" % sql
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
    except (mysql.OperationalError, mysql.ProgrammingError), c:
        # sqlErr return 1
        print c
        if "cur" in dir():
            cur.close()
        return 1
    else:
        conn.commit()
        cur.close()
        return res


# 初始化数据库, 建库, 建表, 创建管理员账号
def init_db(u_pwd):
    conn = mysql.connect(host=host, port=port, user=user, passwd=pwd)
    # 建库
    create_db = "create database day7"
    # 建表
    createtable = "create table day7.day7_homework(id int(5) not null " \
                  "AUTO_INCREMENT PRIMARY key , ip varchar(18), webstatus varchar(10), num int(5));"
    create_user_table = "create table day7.user(id int(3) not null AUTO_INCREMENT PRIMARY key, u_name varchar(20), " \
                  "u_pwd varchar(20))"
    # 创建管理员账号
    create_user = r"insert into day7.user(u_name, u_pwd) values ('admin', '%s')" % u_pwd

    cur = conn.cursor()

    try:
        cur.execute(create_db)
        cur.execute(createtable)
        cur.execute(create_user_table)
        cur.execute(create_user)
        conn.commit()
    except (mysql.ProgrammingError, mysql.OperationalError), c:
        print c
        # 如果表已经存在了, 则删除数据库后, 重新创建
        cur.execute("drop database day7")
        conn.commit()
        # 递归调用, 重新初始化
        init_db(u_pwd)
    else:
        cur.close()


# 玩儿.....噗噗噗噗噗
def test():
    print "host:%s, port:%s, user:%s, pwd:%s" % (host, port, user, pwd)


if __name__ == '__main__':
    pass
