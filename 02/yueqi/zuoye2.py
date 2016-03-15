#! /usr/bin/python
arr = [3,1,4,5,10,2]
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if arr[i] > arr[j]:
			arr[i],arr[j]=arr[j],arr[i]
print arr
input=0
while True:
	start=0
	end=len(arr)-1
	input=int(raw_input("Input:"))
	position=end/2
	while True:
		if arr[position] < input:
			start=start+1
			position=(start+end)/2
			if arr[position] >= input and position <= end:
				arr[position:position]=[input]
				break
			elif position not in range (end):
				arr.append(input)
				break
		elif arr[position] > input:
			end=end-1
			position=(start+end)/2
			if arr[position] <= input and position >= start:
				arr[position+1:position+1]=[input]
				break
			elif position not in range (end):
				arr[0:0]=[input]
				break
	print arr 
