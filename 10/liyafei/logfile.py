#!/usr/bin/python
import sql
import config
db = sql.DB(config.db,config.db_host,config.db_user,config.db_passwd)
dt = {}
with open('tmp.log') as f:
        while True:
            line = f.readline().split()
            if line:
                ip,status = line[0],line[8]
                dt[(ip,status)] = dt.get((ip,status),0)+1
            else:break
for l in sorted(dt.items() ,key=lambda x:-x[1])[:100]:
        ip_tmp, status_tmp, count_tmp = l[0][0],l[0][1],l[1]
        sql = "insert into data (ip,status,count) values (\'%s\',\'%s\',\'%s\')" % (ip_tmp,status_tmp,count_tmp)
        print sql
        db.execute(sql)
