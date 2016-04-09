#!/usr/bin/env python
#coding: utf-8

wen=open('www_access_20140823.log')
tmp=wen.readlines()
wen.close()

res_dict= {}
for i in range(len(tmp)):
        tttt = tmp[i].split(' ')[0],tmp[i].split(' ')[6],tmp[i].split(' ')[8]
        res_dict[tttt] = res_dict.get(tttt,0) + 1



new_dict = {}

for key,val in res_dict.items():
     new_dict.setdefault(val,[])
     new_dict[val].append(key)


rt='''
        <tr>
             <td>%s</td>
             <td>%s</td>
             <td>%s</td>
             <td>%s</td>
             <td>%s</td>
        </tr>
'''
wen= open('ss.html','a+')
count = 1
key_list = new_dict.keys()
wen.write('<table border="1">')
wen.write(rt %('NO','ip','path','status','count'))
while count<11:
       max_val = max(key_list)
       if len(new_dict[max_val]) == 1:
            wen.write(rt % (count,new_dict[max_val][0][0],new_dict[max_val][0][1],new_dict[max_val][0][2],max_val))
            count = count +1
            key_list.remove(max_val)
       else:
           for key in range(len(new_dict[max_val])):
                   wen.write(rt % (count,new_dict[max_val][key][0],new_dict[max_val][key][1],new_dict[max_val][key][2],max_val))
           count = count + len(new_dict[max_val])
           key_list.remove(max_val)
wen.write('</table>')
wen.close()
