#!/bin/env python
# coding=utf-8

import mysqldb as db


def adduser(username,password):
	sql = "insert into user(name,password) values('%s','%s')"%(username,password)
	count = db.execute(sql)
	return count


def edituser(userid,password):
	sql = "update user set password='%s' where id=%s"%(password,userid)
	count = db.execute(sql)
	return count


def deluser(userid):
	sql = "delete from user where id=%s"%(userid)
	count = db.execute(sql)
	return count


def userlist(order='name'):
	sql = "select id,name,password from user order by %s"%(order)
	res = db.select_all(sql)
	return res


def userlist_by_page(order='name',page_int=1,page_size=10):
	sql = "select id,name,password from user order by %s"%(order)
	res = db.select_by_page(sql,page_int,page_size)
	return res


def user_by_id(userid):
	sql = "select id,name,password from user where id=%s"%(userid)
	res = db.select_one(sql)
	return res


def countuser():
	sql = "select id,name,password from user"
	count = db.countselect(sql)
	return count