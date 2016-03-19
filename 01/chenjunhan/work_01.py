#!/usr/bin/env python
# coding=utf-8
num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
a = 0
b = 0


"""
for i in num_list:
    if i > a:
        b = a
        a = i
    elif i > b:
        b = i
print a,b
"""


for n in num_list:
    if n > a:
        a = n
for n in num_list:
    if n > b and n < a:
        b = n
print a,b



