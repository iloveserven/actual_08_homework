#!/bin/env python
# coding=utf-8

import MySQLdb

try:
    conn = MySQLdb.connect(host='180.153.191.128',user='reboot',passwd='reboot123',port=3306,db='zhugaojian',charset="utf8",autocommit=True)
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def countselect(sql):
    try:
        cur.execute(sql)
        return cur.rowcount
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_all(sql):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_by_page(sql,page_int=1,page_size=10):
    try:
        sql = 'select * from (%s) t limit %s,%s'%(sql,(int(page_int)-1)*int(page_size),int(page_size))
        cur.execute(sql)
        return cur.fetchall()
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_one(sql):
    try:
        cur.execute(sql)
        return cur.fetchone()
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def select_many(sql,size=None):
    try:
        cur.execute(sql)
        return cur.fetchmany(size=size)
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def execute(sql):
    try:
        count = cur.execute(sql)
        return count
    except MySQLdb.Error, e:
        print "Mysql Error:%s\nSQL:%s"%(e,sql)


def close():
    try:
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error:%s"%(e)