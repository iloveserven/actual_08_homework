#!/usr/bin/env python

list1=[1,2,3,2,65555,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,234]

list2=[]
b=0
for value1 in list1:
    if len(list2)==0:
        list2=[value1]
    else:
        for index_list2 in range(len(list2)):
            a=len(list2)
            if list2[index_list2]>=value1:
                list2.insert(index_list2,value1)
                b=len(list2)-1
                break
        if a!=b:
            list2.append(value1)
print list2
