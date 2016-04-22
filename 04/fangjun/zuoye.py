#!/usr/bin/python27
#encoding=utf-8
fname = "www_access_20140823.log"
res = {}
#读取文件，取出ip,uri,status三个字段，组合成一个字符串，放到字典中
with open(fname) as f:
    for line in f.readlines():
        line = line.strip('\n').split()
        str = "%s,%s,%s"% (line[0],line[6],line[8])
        res[str] = res.get(str,0) + 1

#字典反转
new_res = {}
for key,val in res.items():
    new_res.setdefault(val,[])
    new_res[val].append(key)

#字符串模板
str = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
"""
tmp = "<table border='1'>"

#字符串拼接
tmp += str %('ip','uri','status','number')

count = 1
key_arr = new_res.keys()
while count < 10:
    if len(key_arr) == 0:
        break
    max_count = max(key_arr)
    for uri in new_res[max_count]:
        uri_tmp = uri.split(',')
        #print '%s,%s,%s,%s' %(uri_tmp[0],uri_tmp[1],uri_tmp[2],max_count)
        tmp += str %(uri_tmp[0],uri_tmp[1],uri_tmp[2],max_count)
    key_arr.remove(max_count)
    count += len(new_res[max_count])
    
tmp += "</table>"
#print tmp
with open('uri.html','w') as f:
    f.write(tmp)
