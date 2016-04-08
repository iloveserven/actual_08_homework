#coding:utf-8
'''
读取文件，过滤出ip，url, code
'''
new_dict = {}
with open('www_access_20140823.log') as f:
	for i in f.readlines():
		arr = i.split()
		new_dict[(arr[0],arr[6],arr[8])] = new_dict.get((arr[0],arr[6],arr[8]),0) +1


'''
字典反转
'''
res_dict = {}
for key,val in new_dict.items():
	res_dict.setdefault(val,[])
	res_dict[val].append(key)


'''
转换成list，排序，取出前十位写进zuoye.html里
'''
str_body = '''  
	<!DOCTYPE HTML>
	<html>
	<link href="http://cdn.bootcss.com/ink/3.1.10/css/ink-flex.min.css" rel="stylesheet">
	<table border='2' >
'''

temp = '''
	<tr align='center'>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
	</tr>
'''
str_body += temp %('count','IP','URL','CODE')

res_list = list(res_dict.items())

res_list.sort()
arr =  res_list[-1:-11:-1]

for i in arr:
	str_body += temp %(i[0],i[1][0][0],i[1][0][1],i[1][0][2])

str_body += '''
	</table>
	</html>
'''

print str_body

with open('zuoye.html','w+') as f2:
	f2.write(str_body)
 
