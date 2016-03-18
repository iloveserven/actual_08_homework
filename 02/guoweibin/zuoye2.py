# -*- coding: utf-8 -*-
arr=[3,1,4,5,10,2]
#遍历list，假设arr[min_index]值最小
for i in range(len(arr)):
    min_index=i
#与后面的进行比较，如果 arr[min_index]大于后面值，则后面为最小
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
#交换两个值
    arr[i],arr[min_index]=arr[min_index],arr[i]
print str(arr)