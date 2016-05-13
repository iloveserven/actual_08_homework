#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Other: suli
# Time: 2016.04.29 16:00
#
#
import operation_dbs


# 查询用户
def get_user(username=""):
    sql = r"select * from day7.user where u_name='%s'" % username
    if username == "":
        sql = r"select * from day7.user"
    return operation_dbs.execute_mysql(sql)


# 创建
def create_user(username, pwd):
    sql = r"insert into day7.user (u_name, u_pwd) values('%s','%s');" % (username, pwd)
    return operation_dbs.execute_mysql(sql)


# 修改用户
def update_user(u_id, pwd):
    sql = r"update user set u_pwd='%s' where id=%s" % (pwd, u_id)
    return operation_dbs.execute_mysql(sql, True)


# 删除
def del_user(u_id):
    sql = r"delete from user where id=%s" % u_id
    return operation_dbs.execute_mysql(sql)





