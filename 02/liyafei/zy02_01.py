#!/usr/bin/python
arr = []
count = 0
while True:
    num = raw_input('Please input Num or Enter(exit) : ')
    if len(num) == 0:
        print 'END'
        break
    num = int(num)
    if count == 0:    
        arr.append(num)
        count+=1
        print arr
    else:
        for i in range(len(arr)):
            if num < arr[i]:
                arr.insert(i,num)
                print arr
                break
            elif num > arr[-1]:
                arr.append(num)    
                print arr
