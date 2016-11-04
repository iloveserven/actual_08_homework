# -*- coding:utf-8 -*-

arr = [3,1,4,5,10,2,11,6,234,128]
L = range(1,len(arr))

for i in L:
    while arr[i]<arr[i-1] and i!=0:
        arr[i],arr[i-1] = arr[i-1],arr[i]
        i-=1
    print arr
