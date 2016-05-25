#!/bin/env python
#coding:utf-8

line_dict = {}
with open('www_access_20140823.log') as f:
    for line in f.readlines():
        tmp = line.split(' ')
        tmp_tuple=(tmp[0],tmp[6],tmp[8])
        line_dict[tmp_tuple]=line_dict.get(tmp_tuple,0)+1

reverse_dict={}
for k,v in line_dict.items():
    reverse_dict.setdefault(v,[]).append(k)

v_list = reverse_dict.keys()

html_str='<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet"> <table class="table table-striped">'
tmp_str = '''
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
'''
html_str += tmp_str%('NO','IP','url','status','count')

count = 1
while count<11:
    max_value = max(v_list)
    v_list.remove(max_value)
    #print count,max_value,reverse_dict[max_value]
    for i in range(len(reverse_dict[max_value])):
        html_str += tmp_str%(count,reverse_dict[max_value][i][0],reverse_dict[max_value][i][1],reverse_dict[max_value][i][2],max_value)
        #print count,reverse_dict[max_value][i][0],reverse_dict[max_value][i][1],reverse_dict[max_value][i][2],max_value
    count += len(reverse_dict[max_value])
html_str += '</table>'

with open('access_count.html','w') as f:
    f.write(html_str)