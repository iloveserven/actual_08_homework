#!/usr/bin/env python
# -*- coding:utf-8 -*-

arr = [3, 1, 4, 5, 10, 2, 6, 55, 88, 99, 100]
for n in range(len(arr)):
    min = n
    for j in range(n + 1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[n], arr[min] = arr[min], arr[n]
print str(arr)
