#!/usr/local/bin/python
arr = [9,7,6,4,7,5,4,7,8,5,3,21,3,5,7,1,0]
for i in range(1,len(arr)):
  for j in range(i):
    if arr[i] < arr[j]:
      arr.insert(j,arr.pop(i))
print arr
