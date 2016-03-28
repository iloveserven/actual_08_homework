#!/bin/env python

arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
first_max_num=0
second_max_num=0
for n in arr:
    n=int(n)
#    print n
    if n>=first_max_num:
        second_max_num=first_max_num
        first_max_num=n
    elif n>=second_max_num:
        second_max_num=n
print 'first max number is %s,second max number is %s.'%(first_max_num,second_max_num)
