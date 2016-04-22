#!/usr/bin/env python
#-^- coding:utf-8 -^-
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num = 0
second_num = 0
"""
for k in arr:
    if k > max_num:
        max_num = k
for k in arr:
    if k == max_num:
        continue
    if k > second_num:
        second_num = k
print 'max_num %d, second_num %d' % (max_num, second_num)

"""
for k in arr:
    if k > max_num:
        second_num = max_num
        max_num = k
    elif k > second_num:
        second_num = k
print 'max_num %d, second_num %d' % (max_num, second_num)