#!/usr/bin/python
import MySQLdb as mysql
import config

class DB():
    def __init__(self,db,host,user,passwd):
        self.db = db
        self.host = host
        self.user = user
        self.passwd = passwd
        self.connect()
    def connect(self):
        self.con = mysql.connect(db=self.db,charset='utf8',host=self.host,user=self.user,passwd=self.passwd)
        self.cursor = self.con.cursor()
        self.con.autocommit(True)
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception,e:
            try:
                self.con.close()
                self.cursor.close()
            except:
                pass
            self.connect()
            self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print res
        return res
