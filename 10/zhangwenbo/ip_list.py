import MySQLdb as mysql
con = mysql.connect(db='web',host='localhost',user='root',passwd='mysql')
con.autocommit(True)
cursor = con.cursor()
sql = "insert into log(ip,status,count) values('%s','%s','%s')"

f = open('www_access_20140823.log')
ad ={}
for i in f:
	arr = i.split(' ')
	ad[(arr[0],arr[8])] = ad.get((arr[0],arr[8]),0)+1

res_list = [(k[0],k[1],v) for k,v in ad.items()]


count = 0
for i in range(len(res_list)-1):
	for j in range(len(res_list)-1-i):
		if res_list[j][2]>res_list[j+1][2]:
			res_list[j],res_list[j+1] = res_list[j+1],res_list[j]	
	now_max,pre_max = res_list[-(i+1)],res_list[-i]
	if now_max[2]==pre_max[2]:
		count = count+1
	else:
		count = 0
	if i >99:
		break
	cursor.execute(sql % (now_max[0],now_max[1],now_max[2]))

con.commit()