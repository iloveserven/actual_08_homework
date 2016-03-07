#/usr/bin/env python
#-*- coding:utf-8 -*-

l = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

t = 0
n = 0

for i in l:
    if  i >= t:
        n = t
        t = i
    elif  i >= n:
        n = i


print t ,n
