#!/usr/bin/env python
# coding=utf-8
#通过sort实现插入排序
'''
def insert(b,a=None):
    a.append(b)
    #排序
    a.sort()
    #反转
    #a.reverse()
    print a
input = raw_input("请输入数字: ")
arr = [3,1,5,7,10,2]
insert(int(input),a=arr)
'''

#通过冒泡拍训实现插入排序
arr = [3,1,5,7,10,2]
count = 0
while True:
    input=raw_input("Please input your num or 'exit': ")
    if input == "exit":
        break
    input=int(input)
    arr.append(input)
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            count = count + 1
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
print arr
print count



