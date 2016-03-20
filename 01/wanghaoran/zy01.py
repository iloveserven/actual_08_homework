#!/usr/bin/python
#-*- coding:utf-8 *-*
#列出list最大和第二大数字，如第二大和最大相同，则把两个数字都列出来
arr = [2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45] 
num1 = 0
num2 = 0
for i in arr:
    if i >= num1:
    	num2 = num1
    	num1 = i
    elif num2 < i < num1:
		num2 = i
print "最大的数字是%s，第二大的数字是%s"%(num1,num2)