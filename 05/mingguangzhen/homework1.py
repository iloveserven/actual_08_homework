#encoding=utf8
# 筛选出列表中的数字和运算符
calc_str = '2+3*8+7*12-100+11+5'
def sign_filter(calc_str=calc_str):
	tmp_list = list(calc_str)
	sign_list = []
	for _str in tmp_list:
		if _str in ['+','-','*','/']:
			sign_list.append(_str)
	return sign_list
# print sign_filter(calc_str)

def num_filter(calc_str=calc_str):
	num_list = []
	str_list = []
	for sign in ['+','-','*','/']:
		calc_str = calc_str.replace(sign, ' ')
	str_list = calc_str.split(' ')
	for num in str_list:
		num_list.append(int(num))
	return num_list
# print num_filter(calc_str)

# 计算列表运算后的值
def clac():
	num_list = num_filter()
	sign_list = sign_filter()
	length = len(sign_list)
	for sign in sign_list:
		if sign == '+':
			num_list[0] = num_list[0] + num_list[1]
			num_list.remove(num_list[1])
		elif sign == '-':
			num_list[0] = num_list[0] - num_list[1]
			num_list.remove(num_list[1])
		elif sign == '*':
			num_list[0] = num_list[0] * num_list[1]
			num_list.remove(num_list[1])
		elif sign == '/':
			num_list[0] = num_list[0] / num_list[1]
			num_list.remove(num_list[1])
	return num_list[0]

	# length = len(sig_list)
	# while res < length:
	# 	nu_list[0] = int(nu_list[0])
	# 	if sig_list.pop(0) == '+':
	# 		nu_list[0] += int(nu_list.pop(1))
	# 		print nu_list[0]
	# 	elif sig_list.pop(0) == '-':
	# 		nu_list[0] -= int(nu_list.pop(1))
	# 		print nu_list[0]
	# 	elif sig_list.pop(0) == '*':
	# 		nu_list[0] *= int(nu_list.pop(1))
	# 		print nu_list[0]
	# 	elif sig_list.pop(0) == '/':
	# 		nu_list[0] /= int(nu_list.pop(1))
	# 		print nu_list[0]
	# 	res += 1
	# return nu_list[0]
print clac()
