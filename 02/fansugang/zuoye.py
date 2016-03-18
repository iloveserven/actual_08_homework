arr  = [1,3,2,10,7,12,22,33,9]
for i in range(len(arr)-1):
	for j in range(i+1,len(arr)):
		if arr[i] > arr[j]:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
	print arr