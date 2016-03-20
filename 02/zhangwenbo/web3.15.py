#coding=utf-8
arr = [3,1,4,5,10,2]
for x in range(1, len(arr)):
	for i in range(x,0,-1):
		if arr[i] < arr[i - 1]:
			arr[i], arr[i - 1] = arr[i - 1], arr[i]
		else:
			break		
print arr