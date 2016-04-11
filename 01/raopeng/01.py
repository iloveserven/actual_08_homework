#!/usr/bin/env python
#coding:utf8
#arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,65555]
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,2000000]
num1 = 0
num2 = 0
for i in arr:
    if i > num1:
        num2 =num1
        num1 = i 
    elif i >= num2:
        num2 = i
print num1,num2
