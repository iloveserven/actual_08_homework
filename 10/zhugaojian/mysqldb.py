#!/bin/env python
# coding=utf-8

import MySQLdb
import time
import config

class DB():
    def __init__(self,host=config.host,user=config.user,passwd=config.passwd,port=config.port,db=config.db,charset=config.charset,autocommit=config.autocommit):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.charset = charset
        self.autocommit = autocommit
        self.connect()

    def connect(self):
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,port=self.port,db=self.db,charset=self.charset,autocommit=self.autocommit)
            self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def tryexecute(self,sql):
        try:
            count = self.cur.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            try:
                self.cur.close()
                self.conn.close()
            except:
                pass
            time.sleep(1)
            try:
                self.connect()
                count = self.cur.execute(sql)
            except (AttributeError, MySQLdb.OperationalError):
                time.sleep(2)
                self.connect()
                count = self.cur.execute(sql)
        return count

    def countselect(self,sql):
        try:
            self.tryexecute(sql)
            return self.cur.rowcount
        except MySQLdb.Error, e:
            print "Mysql Error:%s\nSQL:%s"%(e,sql)


    def select_all(self,sql):
        try:
            self.tryexecute(sql)
            return self.cur.fetchall()
        except MySQLdb.Error, e:
            print "Mysql Error:%s\nSQL:%s"%(e,sql)


    def select_by_page(self,sql,page_int=1,page_size=10):
        try:
            sql = 'select * from (%s) t limit %s,%s'%(sql,(int(page_int)-1)*int(page_size),int(page_size))
            self.tryexecute(sql)
            return self.cur.fetchall()
        except MySQLdb.Error, e:
            print "Mysql Error:%s\nSQL:%s"%(e,sql)


    def select_one(self,sql):
        try:
            self.tryexecute(sql)
            return self.cur.fetchone()
        except MySQLdb.Error, e:
            print "Mysql Error:%s\nSQL:%s"%(e,sql)


    def select_many(self,sql,size=None):
        try:
            self.tryexecute(sql)
            return self.cur.fetchmany(size=size)
        except MySQLdb.Error, e:
            print "Mysql Error:%s\nSQL:%s"%(e,sql)


    def execute(self,sql):
        try:
            count = self.tryexecute(sql)
            return count
        except MySQLdb.Error, e:
            print "Mysql Error:%s\nSQL:%s"%(e,sql)


    def close(self):
        try:
            self.cur.close()
            self.conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error:%s"%(e)