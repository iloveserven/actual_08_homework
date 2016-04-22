#!/usr/bin/env python
arr = [1,2,3,10,7,9,22,33,12]

for i in range(1,len(arr)):
     for y in range(i):
        if arr[i] > arr[y]:
           arr.insert(y,arr.pop(i))
print arr
