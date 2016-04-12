# -*- coding: utf-8 -*-
import sys

log_dict={}
result=[]
##打开文件，并将用户Ip，访问连接,访问状态作为keys，出现次数作为values，形成字典
try:
    with open('www_access_20140823.log') as f:
          for line in f:
               state_list=line.split()
               log_dict.setdefault((state_list[0],state_list[6],state_list[8]),0)
               log_dict[state_list[0],state_list[6],state_list[8]]+=1
          # print log_dict
except IOError as e:
    print "The log file is not exist"
    sys.exit(1)

#将形成的结果字典反转
new_dict={}
for key,val in log_dict.items():
    new_dict.setdefault(val,[])
    new_dict[val].append(key)
# print new_dict


res_str='<table border="1" align="center">'
tmp=''' <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>'''
res_str+=tmp%('排名','访问次数','用户IP','访问链接','访问HTTP状态')

count=1
key_var=new_dict.keys()
str_list=[]

while count<11:
    max_count=max(key_var)
    length=len(new_dict[max_count])

    if length==1:
      res_str+=tmp%(count,max_count,new_dict[max_count][0][0],new_dict[max_count][0][1],new_dict[max_count][0][2])
    elif length>1:
        for i in range(length):
           res_str+=tmp%(count,max_count,new_dict[max_count][i][0],new_dict[max_count][i][1],new_dict[max_count][i][2])
    key_var.remove(max_count)


    count=count+len(new_dict[max_count])
res_str+='</table>'
f=open('zuoye4.html','w')
f.write(res_str)
f.close()





