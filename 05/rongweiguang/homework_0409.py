#!/usr/bin/python
#!coding:utf-8
def app(str):
#将获取的str拆分成两个list，一个存放数值，另一个存放运算符
        tmp_lst = list(str)
        num_lst = []
        num_str = ''
        code_lst = []
        for i in tmp_lst:
                if i not in ['+','-','*','/']:
                        num_str += i
                else:
                        num_lst.append(num_str)
                        code_lst.append(i)
                        num_str = ''
        num_lst.append(num_str)
#遍历处理两个list，计算结果
        res = int(num_lst[0])
        for i in range(len(code_lst)):
                if code_lst[i] == '+':
                        res += int(num_lst[i+1])
                elif code_lst[i] == '-':
                        res -= int(num_lst[i+1])
                elif code_lst[i] == '*':
                        res *= int(num_lst[i+1])
                else:
                        res /= int(num_lst[i+1])
        return res

input_str = raw_input('Please input your str: ')
print '%s == %s '%(input_str,app(input_str))
