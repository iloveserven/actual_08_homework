#!/bin/env python
# coding=utf-8
import mysqldb as db

access_dict = {}
rev_dict = {}
res_dict = {}

def get_max_many(max_many=10):
	with open('www_access_20140823.log') as f:
		for line in f:
			tmp = line.split(' ')
			tmp_tup = (tmp[0],tmp[8])
			access_dict[tmp_tup] = access_dict.get(tmp_tup,0)+1

	for k,v in access_dict.items():
		rev_dict.setdefault(v,[]).append(k)

	v_list = rev_dict.keys()
	count = 1

	while count <= max_many:
		max_value = max(v_list)
		v_list.remove(max_value)
		res_dict[max_value] = rev_dict[max_value]
		count = count+len(res_dict[max_value])


def del_all():
	sql = "delete from access_log_statistics"
	count = db.execute(sql)
	return count


def insert_access():
	count = 0
	for k,v in res_dict.items():
		for i in v:
			sql = "insert into access_log_statistics(ip,status,access_num) values('%s','%s',%s)"%(i[0],i[1],k)
			count += db.execute(sql)
	return count


def access_log_list(order='access_num desc'):
	sql = "select id,ip,status,access_num from access_log_statistics order by %s"%(order)
	res = db.select_all(sql)
	return res


def count_access_log():
	sql = "select id,ip,status,access_num from access_log_statistics"
	count = db.countselect(sql)
	return count


def access_log_list_by_page(order='access_num',page_int=1,page_size=10):
	sql = "select id,ip,status,access_num from access_log_statistics order by %s"%(order)
	res = db.select_by_page(sql,page_int,page_size)
	return res


if __name__ == '__main__':
	get_max_many(100)
	print del_all()
	print insert_access()
	print len(access_dict)
	print len(rev_dict)
	print len(res_dict)