#!/usr/bin/python

arr = [3,1,2,1,6,7,7,8,5,10,2]
sort_arr= [arr[0]]

for n in range(1,len(arr)):
    for i in range(len(sort_arr)):
        if arr[n] <= sort_arr[i]:
            sort_arr.insert(i,arr[n])
            break
        elif arr[n] > sort_arr[-1]:
            sort_arr.append(arr[n])
print sort_arr


arr01 = [3,1,2,1,6,7,7,8,5,10,2]
for i  in range(1,len(arr01)):
    for n in range(i):
        if arr01[i] < arr01[n]:
            arr01.insert(n,arr01.pop(i))
#            break
#        elif arr01[i] > arr01[i-1]:
#            arr01.insert(i,arr01.pop(i))
#            break
print arr01
