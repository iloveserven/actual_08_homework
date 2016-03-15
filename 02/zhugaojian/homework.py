#!/bin/env python
arr = [3,1,4,5,3,10,2]
print arr
length=len(arr)
curr=1
while curr < length:
    j=curr
    insert_pos=curr
    if j-1==0:
        if arr[curr] < arr[j-1]:
            insert_pos=j-1
    else:
        while True:
            if arr[curr] > arr[j-1]:
                break
            elif arr[curr] < arr[j-1] and arr[curr] >= arr[j-2]:
                insert_pos=j-1
                break
            else:
                j=j-1
    if insert_pos < curr:
        arr.insert(insert_pos,arr.pop(curr))
    curr=curr+1
print arr