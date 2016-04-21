def oper(s):
	arr = split_val(s)
	return cal(arr)

oper_dict = {
	'+':lambda x,y:x+y,
	'-':lambda x,y:x-y,
	'*':lambda x,y:x*y,
	'/':lambda x,y:x/y
}

def split_val(s):
	arr = []
	tmp = ''
	for i in s:
		if i in oper_dict:
			arr.append(tmp)
			tmp = ''
		tmp += i
	arr.append(tmp)
	#print arr
	return arr

def cal(arr):
	#print arr
	init = arr.pop(0)
	for i in arr:
		init = oper_dict[i[0]](int(init),int(i[1:]))
	print init

oper('10+2*4')

