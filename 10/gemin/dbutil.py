#coding:utf-8
__author__ = 'hdd'

import MySQLdb
conn = None
cursor = None

def connect():
    global conn
    global cursor
    conn = MySQLdb.connect(db='gg', port=3306, host='localhost', user='hdd', passwd='123456')
    conn.autocommit(True)
    cursor = conn.cursor()


def execute_sql(sql):
    try:
        cursor.execute(sql)
        print cursor
    except Exception,e:
        print str(e)
        print '重新连接数据库'
        connect()
        cursor.execute(sql)

    return cursor.fetchall()


