#!/usr/bin/env python
# coding:utf8

list_number = [1, 2, 3, 2, 3, 1, 3, 21, 2, 2, 3, 41161,
               22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]
number_max1 = 0
number_max2 = 0

for i in list_number:
    if i > number_max1:
        number_max1 = i

new_list = list_number
new_list.remove(number_max1)

for i in new_list:
    if i > number_max2:
        number_max2 = i

print number_max1, number_max2
