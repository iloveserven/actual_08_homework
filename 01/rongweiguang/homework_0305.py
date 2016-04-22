#!/usr/bin/python
#-*- coding = utf-8 -*-

list_tmp = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
dict_tmp = {}
tmp = list_tmp[0]

for i in list_tmp:
        if i not in dict_tmp:
                dict_tmp[i] = 1
        else:
                dict_tmp[i] = dict_tmp[i] + 1

for i in list_tmp:
        if tmp < i:
                tmp = i
max = tmp
tmp = list_tmp[0]

if dict_tmp[max] != 1:
        print 'zui da shi :%s , di er da ye shi: %s'%(max,max)
else:
        for i in list_tmp:
                if i < max and i > tmp:
                        tmp = i
        print 'zui da shi: %s , di er da shi: %s'%(max,tmp)
