#/usr/bin/env python
#-*- coding:utf-8 -*-
top_dict = {}
count = 0

for line in open('www_access_20140823.log'):
	tmp_tup =  line.split(' ')[0],line.split(' ')[6],line.split(' ')[8]
#	tmp_tup = (f.readline().split(' ')[0],f.readline().split(' ')[6],f.readline().split(' ')[8])
	top_dict[tmp_tup] = top_dict.get(tmp_tup,0)+1

new_res = {}
for key,val in top_dict.items():
 	new_res.setdefault(val,[])
 	new_res[val].append(key)
count = 1
key_arr = new_res.keys()   	
res = open('a.html','w')
res.write('<table border=\'1\'>\n')
res.write('<tr><td>NO</td>\n<td>count</td>\n<td></td></tr>')
while count < 11:
	max_count = max(key_arr)
	res.write('<tr><td>%s</td>\n<td>%s</td>\n<td>%s</td></tr>' %(count,max_count,new_res[max_count]))
	key_arr.remove(max_count)
	count = count + len(new_res[max_count])
res.write('</table>')
res.close
