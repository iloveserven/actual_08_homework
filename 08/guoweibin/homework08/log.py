import  dbutil

res={}
for  line  in open('www_access_20140823.log'):
                      tmp=line.split(' ')
                      user_ip,user_state=tmp[0],tmp[8]
                      res[(user_ip,user_state)]=res.get((user_ip,user_state),0)+1

for   l   in sorted(res.items(),key=lambda  x: -x[1])[:100]:
                sql = 'Insert into log (ip,status,count) values ("%s","%s","%s")' %(l[0][0],l[0][1],l[1])
                print sql
                dbutil.execute(sql)

            