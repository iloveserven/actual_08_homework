#coding=utf-8

res_str = '<table border="1">'
tmp = '''
  <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
  </tr>'''
#定义字典dist
dict={}
f = open('www_access_20140823.log')
for line in f.read().strip().split('\n'):
    file = line.split()
   # print file 
    dict[(file[0],file[6],file[8])] = dict.get((file[0],file[6],file[8]),0)+1
   # print dict
#将字典，转换成列表
res_list = dict.items()
#print res_list
#冒泡排序
length=len(res_list)
count=0
for i in range(length-1):
    for j in range(length-1-i):
        if res_list[j][1] > res_list[j+1][1]:
            res_list[j],res_list[j+1]=res_list[j+1],res_list[j]
    now_max,pre_max = res_list[-(i+1)],res_list[-i]
    if now_max[1]==pre_max[1]:
        count = count +1
    else:
        count =0
        if i>10:
            break
    
#print '第%s名，IP%s,访问url %s ,状态码%s, 次数%s '%(i+1-count,now_max[0][0],now_max[0][1],now_max[0][2],now_max[1])
    res_str += tmp % (i+1-count,now_max[0][0],now_max[0][1],now_max[0][2],now_max[1])  

#写入到html中
res_str += tmp %('NO','IP','url','state','count')
res_str+='</table>'
f = open('test.html','w')
f.write(res_str)
f.close
print "finish"
