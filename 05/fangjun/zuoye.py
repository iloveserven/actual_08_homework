#!/usr/bin/python27
#encoding=utf-8
import string
digits = string.digits
def oper(s):
    num_list = []
    opt_list = []
    for i in s:
        if i in digits:
            num_list.append(int(i))
        else:
            opt_list.append(i)

    result = num_list[0]
    for i in range(1,len(num_list)):
        for j in opt_list:
            if j == '+':
                result += num_list[i]
                opt_list.remove(j)
                break
            if j == '-':
                result -= num_list[i]
                opt_list.remove(j)
                break
            if j == '*':
                result *= num_list[i]
                opt_list.remove(j)
                break
            if j == '/':
                result /= num_list[i]
                opt_list.remove(j)
                break
    return '%s=%s' %(s,result)

while True:
    s = raw_input("输入一个算术表达式,(Q)uit：")
    if len(s) == 0:continue
    if s.lower() == 'q' or s.lower() == 'quit':
        break
    else:
        print oper(s)
