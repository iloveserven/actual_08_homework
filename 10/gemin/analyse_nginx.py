#coding:utf-8
import dbutil

res = {}
f = open('www_access_20140823.log','r')
for line in f:
    tmp = line.split(' ')
    ip,status = tmp[0],tmp[8]
    res[(ip,status)] = res.get((ip,status),0) + 1


for l in sorted(res.items(),key=lambda x:x[1],reverse=True)[:100]:
    sql = 'insert into log(ip,status,count) values("%s",%s,%s)'%(l[0][0],l[0][1],l[1])
    print sql
    dbutil.execute_sql(sql)

