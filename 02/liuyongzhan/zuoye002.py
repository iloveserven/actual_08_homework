#coding=utf8

arr = [3,1,4,5,10,2]
count = 0
for x in range(len(arr)):
    for i in range(len(arr)-1):
        count += 1
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

print range(len(arr))
print arr
print count
