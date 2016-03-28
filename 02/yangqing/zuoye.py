#/usr/bin/env python
#-*- coding:utf-8 -*-

arr = [3,1,4,5,10,2,11,7,8,15]

arrlen = len(arr)
b = [arr.pop()]

for i in range(arrlen-1):
    key = 0
    for n in range(len(b)):
        if arr[i] < b[0]:
            key = 0
            break
        elif arr [i] > b[n]:
            key = n + 1
        elif arr[i] < b[n]:
            key = n
            break
    b.insert(key,arr[i])

print b
