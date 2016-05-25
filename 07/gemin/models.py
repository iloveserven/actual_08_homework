#coding:utf-8

import MySQLdb

#连接数据库
conn = MySQLdb.connect(host='localhost',user='dog',passwd='since1992',db='gg8')
#获取游标对象
cur = conn.cursor()


#nginx日志入库，统计用户IP和访问状态
def stock():
	res = {}
	with open('www_access_20140823.log','r') as f:
		for line in f:
			tmp = line.split(' ')
			ip,status = tmp[0],tmp[8]
			res[(ip,status)] = res.get((ip,status),0) + 1
	#字典反转
	new_res = {}
	for key,val in res.items():
		new_res.setdefault(val,[])
		new_res[val].append(key)
	arr = new_res.keys()
	count = 0
	while count < 100:
		max_num = max(arr)
		for tup in new_res[max_num]:	
			sql = 'insert into nn(ip,status,times) values("%s",%s,%s);'%(tup[0],tup[1],int(count+1))
			cur.execute(sql)
		count += 1
		arr.remove(max_num)


fields = ['id','ip','status','times']

def show_info():
	sql_fetch_all = 'select %s from nn;'%','.join(fields)
	cur.execute(sql_fetch_all)
	datalist = cur.fetchall()
	return [dict(zip(fields,data)) for data in datalist]


user_fileds = ['username','password']

def show_users():
	sql_get_users = 'select %s from user'% ','.join(user_fileds)
	cur.execute(sql_get_users)
	userlist = cur.fetchall()
	return [dict(zip(user_fileds,user)) for user in userlist]


def login(username,password):
	sql_login = 'select * from user where username="%s" and password="%s"'%(username,password)
#	print sql_login
	cur.execute(sql_login)
	if cur.fetchall():
		return True

		
if __name__ == "__main__":
#	stock()
	cur.close()
	conn.close()


