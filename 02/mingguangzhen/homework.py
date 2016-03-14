#! /usr/bin/env python
#encoding=utf8
#
sort_list = [3,1,4,5,10,2]
#sort_list = []
#min_list = []
max_list = []
count = 1
min_num = ''
max_num = ''
insert_index = ''
length = len(sort_list) - 1
for x in range(0, (length)):
    for y in range(0 ,(length-x)):
        if sort_list[y] > sort_list[y+1]:
            sort_list[y], sort_list[y+1] = sort_list[y+1],sort_list[y]
            
while True:
    max_list = []
    #min_list = []
    new_num = raw_input("Please input your num [must integer]，end of the space: ")
    if new_num == '':
        break
    int_num = int(new_num)
   # if count == 1:
   #     sort_list.append(int_num)
   #     print "The %d time(s) add. Add num is: %d" % (count, int_num)
   #     count += 1
   #     print sort_list
    if int_num <= min(sort_list):
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
        for max_index in sort_list:
            if max_index >= int_num:
                max_list.append(max_index)
        max_num = min(max_list)
        insert_index = sort_list.index(max_num)
        sort_list.insert(insert_index, int_num)
        print "The %d time(s) add. Add num is: %d" % (count, int_num)
        count += 1
        print sort_list
## 下面是第一次的部分代码，有问题，引以为戒……
'''
        for min_index in sort_list:
            if min_index <= int_num:
                min_list.append(min_index)
        min_num = max(min_list)
        insert_index = sort_list.index(min_num)
        sort_list.insert(insert_index+1, int_num)
        print "The %d time(s) add. Add num is: %d" % (count, int_num)
        count += 1
        print sort_list
'''
