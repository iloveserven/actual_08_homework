#!/bin/env python
# coding=utf-8

import MySQLdb
import time

conn = None
cur =None

def connect():
    global conn
    global cur
    try:
        conn = MySQLdb.connect(host='180.153.191.128',user='reboot',passwd='reboot123',port=3306,db='zhugaojian',charset="utf8",autocommit=True)
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def tryexecute(sql):
    try:
        count = cur.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
        try:
            cur.close()
            conn.close()
        except:
            pass
        time.sleep(1)
        try:
            connect()
            count = cur.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            time.sleep(2)
            connect()
            count = cur.execute(sql)
    return count

def countselect(sql):
    try:
        tryexecute(sql)
        return cur.rowcount
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_all(sql):
    try:
        tryexecute(sql)
        return cur.fetchall()
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_by_page(sql,page_int=1,page_size=10):
    try:
        sql = 'select * from (%s) t limit %s,%s'%(sql,(int(page_int)-1)*int(page_size),int(page_size))
        tryexecute(sql)
        return cur.fetchall()
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_one(sql):
    try:
        tryexecute(sql)
        return cur.fetchone()
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_many(sql,size=None):
    try:
        tryexecute(sql)
        return cur.fetchmany(size=size)
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def execute(sql):
    try:
        count = tryexecute(sql)
        return count
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def close():
    try:
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error:%s"%(e)