#!/usr/bin/env python
#-^- coding:utf-8 -^-

list_n = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_x = 0
max_y = 0
newList = []
for x in list_n:
    if x > max_x:
        max_x = x

newList.append(max_x)
list_n.remove(max_x)

for y in list_n:
    if y > max_y:
         max_y = y
newList.append(max_y)
print newList
