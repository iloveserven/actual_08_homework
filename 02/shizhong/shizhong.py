#!/usr/bin/env python

#-^- coding:utf-8 -^-

arr = [3,1,4,5,10,2]

length = len(arr)

while True:
	num = input('enter a num: ')
	for i in range(length):
		if num<arr[i]:
			arr.insert(i,num)
			print arr
			break
		elif num>arr[i]:
			arr.insert(i+1,num)
			print arr
			break