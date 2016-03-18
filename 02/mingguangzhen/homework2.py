#! /usr/bin/env python
#encoding=utf8
#
sort_list = [3,1,4,5,10,2]
count = 0

while True:
    new_num = raw_input("Please input your num [must integer]，end of the 'exit': ")
    count += 1
    if new_num == 'exit':
        break 
    int_num = int(new_num)
    sort_list.append(int_num)
    length = len(sort_list) - 1
    for x in range(0, length):
        for y in range(0, length - x):
            if sort_list[y] > sort_list[y+1]:
                sort_list[y], sort_list[y+1] = sort_list[y+1], sort_list[y]
    print "The %d time insert, Add num is %d." % (count, int_num)
    print sort_list
