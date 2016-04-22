#coding=utf8

# arr = [3,1,4,5,10,2]
# count = 0
# while True:
#     num= raw_input("please input a number:")
#     arr.append(int(num))
#     for x in range(len(arr)):
#         for i in range(len(arr)-1):
#             count += 1
#             if arr[i] > arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#     print arr
#     print count


arr = [3,1,4,5,10,2]
count=0

for x in range(len(arr)):
    for i in range(len(arr)-1):
        count += 1
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print arr
for j in range(len(arr)-1):
    num = raw_input("please input a number:")
    if arr(j) <= num < arr(j+1):
        arr.insert(j,num)
        print arr

