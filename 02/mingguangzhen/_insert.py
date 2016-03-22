#!/usr/bin/env python
#encoding=utf8
sort_list = [5, 4, 3, 2, 1]
length = len(sort_list)
count = 0 
for x in range(1, length):
    count += 1
    print count
    for y in range(1, x+1)[::-1]:
        if sort_list[y] < sort_list[y-1]:
            sort_list[y], sort_list[y-1] = sort_list[y-1], sort_list[y]
        print sort_list
