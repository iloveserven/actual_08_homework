#! /usr/bin/env python
#encoding=utf-8
#
sort_list = []
min_list = []
count = 1
min_num = ''
insert_index = ''

while True:
    min_list = []
    new_num = raw_input("Please input your num: ")
    if new_num == '':
        break
    int_num = int(new_num)
    if count == 1:
        sort_list.append(int_num)
        print "The %d time(s) add. Add num is: %d" % (count, int_num)
        count += 1
        print sort_list
    elif int_num <= min(sort_list):
        sort_list.insert(0, int_num)
        print "The %d time(s) add. Add num is: %d" % (count, int_num)
        count += 1
        print sort_list
    elif int_num >= max(sort_list):
        sort_list.append(int_num)
        print "The %d time(s) add. Add num is: %d" % (count, int_num)
        count += 1
        print sort_list
    else:
        for min_index in sort_list:
            if min_index <= int_num:
                min_list.append(min_index)
                min_num = max(min_list)
                insert_index = sort_list.index(min_num)
        sort_list.insert(insert_index+1, int_num)
        print "The %d time(s) add. Add num is: %d" % (count, int_num)
        count += 1
        print sort_list
