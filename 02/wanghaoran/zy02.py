#!/usr/bin/env python
#-*- coding:utf-8 -*-
#第二次作业，插入排序
arr = [1,12,3,8,5,11,46,22]
for i in range(len(arr)):
	min_index = i
	for j in range(i+1,len(arr)):
		if arr[min_index] > arr[j]:
			min_index = j
		arr[min_index],arr[i]=arr[i],arr[min_index]
print arr
