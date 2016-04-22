#!/usr/bin/python27
#
NumList = [1,0,2,-3,2,65535,12,3,-1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max_num1 = None
max_num2 = None
for num in NumList:
    if num > max_num1:
        tmp = max_num1
        max_num1 = num
        num = tmp
    if max_num1 > max_num2:
        #max_num1,max_num2 = max_num2,max_num1
        tmp2 = max_num1
        max_num1 = max_num2
        max_num2 = tmp2

print "The two largest number is: %d and %d" % (max_num1,max_num2)
