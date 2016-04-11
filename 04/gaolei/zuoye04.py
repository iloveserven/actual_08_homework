# -*- coding: utf-8 -*-
f =  open('www_access_20140823.log')
dic = {} 
arr = f.readlines()
sort_arr = [] #经排序之后生成的list，存放的数据为（排名，key值，统计值）元组
no = 1 #排名
count = 1 #记录某一排名有多少个并列
for line in arr:
    tmp = line.split(' ')
    dic_key = (tmp[0],tmp[6],tmp[8])
    dic[dic_key] = dic.get(dic_key,0)+1 #生成字典
while True:
    max_cot = 0 
    for dic_key in dic: #遍历字典，找出value最大值，记录在max_cot和max_key中
        if dic[dic_key] > max_cot:
            max_key = dic_key
            max_cot = dic[dic_key]
    if not sort_arr: #如果list还没有数据，则直接添加，并在字典中删除最大值
        sort_arr.append((no,max_key,max_cot))
        del dic[max_key]
    else: #判断是否有并列，以及list是否已经超过10
        if max_cot == sort_arr[-1][2]:
            count +=1
            sort_arr.append((no,max_key,max_cot))
            del dic[max_key]
        else:
            if len(sort_arr)>10:
                break
            else:
                no += count
                count = 1
                sort_arr.append((no,max_key,max_cot))
                del dic[max_key]
f.close()
scr_string = '''
<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">       
<table class='table table-striped'>\n
'''
tmp = '''
<tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
</tr>\n
'''
scr_string += tmp % ('NO','string','count')
for line in sort_arr:
    scr_string += tmp % (line[0],line[1],line[2])
scr_string += '</table>\n'
f = open('zuoye.html','w')
f.write(scr_string)
f.close()
    
    
        



    





    
    
    

        
