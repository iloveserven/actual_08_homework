#!/bin/env python
# coding=utf-8

import mysqldb as db


def addserver(name,memory,expired_date,email,note):
    count = 0
    sql = "insert into server(name,memory,expired_date,email,note) values('%s','%s','%s','%s','%s')"%(name,memory,expired_date,email,note)
    try:
        count = db.execute(sql)
    except Exception, e:
        print e
        return 0
    
    return count


def editserver(serverid,name,memory,expired_date,email,note):
    sql = "update server set name='%s',memory='%s',expired_date='%s',email='%s',note='%s' where id=%s"%(name,memory,expired_date,email,note,serverid)
    count = db.execute(sql)
    return count


def delserver(serverid):
    sql = "delete from server where id=%s"%(serverid)
    count = db.execute(sql)
    return count


def serverlist(order='name'):
    sql = "select id,name,memory,expired_date,email,note from server order by %s"%(order)
    res = db.select_all(sql)
    return res


def serverlist_by_page(order='name',page_int=1,page_size=10):
    sql = "select id,name,memory,expired_date,email,note from server order by %s"%(order)
    res = db.select_by_page(sql,page_int,page_size)
    return res


def server_by_id(serverid):
    sql = "select id,name,memory,expired_date,email,note from server where id=%s"%(serverid)
    res = db.select_one(sql)
    return res


def countserver():
    sql = "select id,name,memory,expired_date,email,note from server"
    count = db.countselect(sql)
    return count