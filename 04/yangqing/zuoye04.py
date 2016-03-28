#!/usr/bin/env python
#-*- coding:utf-8 -*-

#统计
dict_log = {}
f = open('www_access_20140823.log')
for i in f.readlines():
    tmp_list = i.split()
    tulpe_key =  (tmp_list[0],tmp_list[6],tmp_list[8])
    dict_log[tulpe_key] = dict_log.get(tulpe_key,0)+1
f.close()

#翻转
new_dict = {}
for key,val in dict_log.items():
    new_dict.setdefault(val,[])
    new_dict[val].append(key)



key_arr = new_dict.keys()
res = """
"<table border='2'>
	<tr>
		<td>NO</td>
		<td>srt</td>
		<td>NUM</td>
	</tr>
"""
#前10名
count = 1
while count <11:
    max_count = max(key_arr)
    for i in new_dict[max_count]:
        str = '\t<tr>\n\t\t<td>%s</td>\n\t\t<td>%s</td>\n\t\t<td>%s</td>\n\t</tr>' %(count,i,max_count)
        res += str
    key_arr.remove(max_count)
    count = count +len(new_dict[max_count])
#生成文件
f = open('web.html','w+')
for i in res:
    f.writelines(i)
f.close()
