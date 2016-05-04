import MySQLdb as mysql
with open('www_access_20140823.log') as f:
        tmp_dict = {}
        for line in f:
                tmp = line.split(' ')
                tmp_str=tmp[0]+' '+tmp[8]
                tmp_dict[tmp_str]=tmp_dict.get(tmp_str,0)+1
res_dict={}
for k,v in tmp_dict.items():
        res_dict.setdefault(v,[]).append(k)
v_list =res_dict.keys()
con =mysql.connect(db='user',host='localhost',user='root',passwd='123')
cursor=con.cursor()
cursor.execute('delete from log')
sql= "insert into log(ip,state,counttime) values('%s','%s','%s')"

count = 0
while count<100:
        max_val = max(v_list)
        v_list.remove(max_val)
        for i in res_dict[max_val]:
                cursor.execute(sql%(i.split(' ')[0],i.split(' ')[1],max_val))
                count += 1
                if count ==100:
                        break
con.commit()
