#!/usr/bin/python27
#       
arr = [3,1,45,10,2]
for j in range(1,len(arr)):
    for i in range(j,0,-1):
        if arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
print arr
        
