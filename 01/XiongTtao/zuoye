#!/usr/bin/env python
#_*_ coding:utf-8 _*_

l = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
d = {}
n = l[0]

for i in l:
       if i not in d:
            d[i] = 1
       else:
            d[i] = d[i]+1

for i in l:
       if n < i:
            n = i


max_sum = n
n = l[0]

if d[max_sum] > 1:
         print 'max  :%s ,max :%s'%(max_sum,max_sum)
else:
       for i in l:
             if i <max_sum and i > n:
                       n = i
       print 'max :%s, max :%s'%(max_sum,n)
