#!/usr/bin/python

lst_num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num1 = 0
max_num2 = 0

for n in lst_num:
    #print n
    if n >= max_num1:
        max_num2 = max_num1
        max_num1 = n
    elif n > max_num2:
        max_num2 = n 
print 'max_num1: %d \nmax_num2: %d' % (max_num1,max_num2)
