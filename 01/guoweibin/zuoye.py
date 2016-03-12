# -*- coding: utf-8 -*-
num_list=[1,2,3,2,12,3,1,3,21,2,2,4,4111,22,3333,444,111,4,5,777,65555,45,33,45]
num_dict={}

first_max=0
second_max=0
#利用dict统计每个数字出现次数
for s in num_list:
    if s in num_dict:
        num_dict[s]=num_dict[s]+1
    else:
        num_dict[s]=1
#求第一个最大值
for key in num_dict:
    if key>first_max:
        first_max=key
print "第一个最大值",first_max

#求第二个最大值
#如果最大值出现多个，则第二个最大值等于第一个最大值
if num_dict[first_max]!=1:
    print "第二个最大值也是",first_max
#最大值出现1次，求第二个最大值
else:
    for key in num_dict:
        if key>second_max and key<first_max and int(num_dict[key])==1:
              second_max=key
    print "第二个最大值",second_max




















