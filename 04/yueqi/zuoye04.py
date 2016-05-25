#! /usr/bin/python
#coding=utf-8
f=open('www_access_20140823.log')
list_f=f.readlines()
f.close()
dict_f={}
dict_f_new={}
list_temp=['s']
k=''
count=0
#将list_f转换为以ip&访问地址&访问码为key的字典,value为该key的出现次数的累加
for i in range(len(list_f)):
	list_temp[0]=list_f[i].split()
	k=list_temp[0][0]+','+list_temp[0][6]+','+list_temp[0][8]
	dict_f[k]=dict_f.setdefault(k,0)+1
#对dict_f重新按value进行排序，并放入dict_f_new
for key,value in dict_f.items():
	dict_f_new.setdefault(value,[])
	if value in dict_f_new:
		dict_f_new[value].append(key)
#对dict_f_new的key进行排序，放入list_new
list_new=['']
start=0
position=0
count=0
for key in dict_f_new:
	end=len(list_new)-1
	position=end/2
	if list_new[0]=='':
		list_new[0]=key
	while True:
		if position == 0:
			for i in range(len(list_new)):
				if key > list_new[i]:
					list_new[i:i]=[key]
					break
			break
		elif list_new[position] < key:
			end=end-1 
			position=end/2
			if list_new[position]>=key and position > 0:
				list_new[position+1:position+1]=[key]
				break
			elif list_new[0]<key:
				list_new[0:0]=[key]
				break
		elif list_new[position] > key:
			start=start+1
			position=(start+end)/2
			if list_new[position]<key:
				list_new[position:position]=[key]
				break
			elif list_new[position]>key and start==end:
				list_new.append(key)
				break
#取出list_new中前10,含并列,输出结果写入html文件
wr='''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'''
f=open('/var/www/html/zuoye04.html','w')
temp=0
list_new_2=[]
f.write('<table border=10><tr></tr><tr><td>IP</td><td>Dest</td><td>code</td><td>count</td></tr>')
for i in range(0,10):
	len(dict_f_new[list_new[i]])
	temp=count
	count = count + len(dict_f_new[list_new[i]])
	if count <= 10:
		for j in range(len(dict_f_new[list_new[i]])):
#			print str(dict_f_new[list_new[i]][j])+','+str(list_new[i])
			list_new_2=dict_f_new[list_new[i]][j].split(',')
			list_new_2.append(str(list_new[i]))
			f.write(wr %(list_new_2[0],list_new_2[1],list_new_2[2],list_new_2[3]))
	elif count > 10:
		temp = 10 - temp
		for j in range(0,temp):
#			print str(dict_f_new[list_new[i]][j])+','+str(list_new[i])
			list_new_2=dict_f_new[list_new[i]][j].split(',')
			list_new_2.append(str(list_new[i]))
			f.write(wr %(list_new_2[0],list_new_2[1],list_new_2[2],list_new_2[3]))
		break
f.write('</table>')
f.close()
