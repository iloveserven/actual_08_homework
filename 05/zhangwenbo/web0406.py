#encoding=utf-8

def oper(s):
	arr =  split_val(s)
	return cal(arr)

oper_dict = {
	'+':lambda x,y:x+y,
	'-':lambda x,y:x-y,
	'*':lambda x,y:x*y,
	'/':lambda x,y:x/y

}

#拆分加减乘除
def splist_val(s):
	arr = []
	tmp = ''
	for i in s:
		if i in oper_dict:
			arr.append(tmp)
			tmp = ''
		tmp +=i
	arr.append(tmp)
	return arr
	
#计算结果
def cal(arr):
	print arr
	init = arr.pop(0)
	for i in arr:
		init = oper_dict[i[0]](int(init),int(i[1:]))
	print init

oper('10+2*3')













