#!/usr/bin/python
import MySQLdb as mysql
from flask import Flask,render_template,request,redirect,session
con = mysql.connect(db='lyfdb',host='localhost',user='lyf',passwd='123')
cursor = con.cursor()

def truncate():
    cursor.execute("truncate table data;")
def insert(ip_tmp,status_tmp,count_tmp):
    cursor.execute("insert into data (ip,status,count) values (\'%s\',\'%s\',\'%s\')" % (ip_tmp,status_tmp,count_tmp))
def select_d():
    page_1=0
    cursor.execute('select count(*) from data')
    page_tmp = cursor.fetchall()
    page_2=page_tmp[0][0]
    cursor.execute('select * from data limit %s,%s' % (page_1*page_2,page_2))
    userlist=cursor.fetchall()
    return userlist
def select_u(username):
        cursor.execute('select * from user where username="%s"' % username)
        userlist=cursor.fetchall()
        return userlist
def select_u_all():
        cursor.execute('select * from user')
        userlist=cursor.fetchall()
        return userlist
def insert_u(user,pwd):
    cursor.execute("insert into user (username,password) values (\'%s\',\'%s\')" % (user,pwd))
def update_u(pwd,id):
    cursor.execute("update user set password='%s' where id='%s'" % (pwd,id))
def user_id(idnum):
    cursor.execute('select username from user  where id=%s' % idnum)
    id_user= cursor.fetchall()
    return id_user
def del_u(idnum):
    cursor.execute('delete from user where id=%s' % idnum)
