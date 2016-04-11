#!/usr/bin/python

f = open('www_access_20140823.log','r')
tmp_arr = f.readlines()
f.close()

sort_dict = {}
res_dict = {}
lst = []
count = 0

#键值互换排序
for i in range(len(tmp_arr)):
	tmp_str = tmp_arr[i].split(' ')[0],tmp_arr[i].split(' ')[6],tmp_arr[i].split(' ')[8]
	sort_dict[tmp_str] = sort_dict.get(tmp_str,0) + 1

for key,val in sort_dict.items():
	if val in res_dict:
		res_val = res_dict[val]
		if isinstance(res_val,list):
			res_val.append(key)
		else:
			res_dict[val] = [res_val,key]
	else:
		res_dict[val] = key

for key in res_dict:
	lst.append(key)

for i in range(1,len(lst)):
	for j in range(1,i+1)[::-1]:
		if lst[j] > lst[j-1]:
			lst[j],lst[j-1] = lst[j-1],lst[j]
		else:
			break
f = open('homework.html','w')
f.write('<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">')
f.write('\n<p align="center">\nHOMEWORK\n</p>\n')
f.write('<table border="1" align="center" width="800px">\n')
f.write('\n<tr>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n</tr>\n'%('IP','URL','STATUS','COUNT'))

#遍历前10，如果不是list直接写入html，如果是list再遍历list写入html，用count和tmp来控制前10的输出
while count<11:
	if isinstance(res_dict[lst[:10][count]],list):
		L = len(res_dict[lst[:10][count]])
		tmp = 10-count
		for j in range(L):
			f.write('\n<tr>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n</tr>\n'%(res_dict[lst[:10][count]][j][0],res_dict[lst[:10][count]][j][1],res_dict[lst[:10][count]][j][2],lst[:10][count]))
			tmp += 1
			if tmp>10:
				break
		count += tmp
	else:
		f.write('\n<tr>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n</tr>\n'%(res_dict[lst[:10][count]][0],res_dict[lst[:10][count]][1],res_dict[lst[:10][count]][2],lst[:10][count]))
		count += 1
f.write('</table>\n')
f.close()
