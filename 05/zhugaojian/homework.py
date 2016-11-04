#!/bin/env python
# coding=utf-8

#作业
##    实现一个函数，可以做加减乘除
##    不考虑优先级
## oper('1+2*3') == 9

string = '10+2*30-3/40'
'''计算值'''
def oper1(arr,f):
    if len(arr)<=3:
        return f(arr)
    else:
        return oper1([f(arr[:3])]+arr[3:],f)


'''把只有三个元素的list计算结果'''

def op(arr):
    if arr[1] == '+':
        return (int(arr[0]) + 0.0) + int(arr[2])
    elif arr[1] == '-':
        return (int(arr[0]) + 0.0) - int(arr[2])
    elif arr[1] == '*':
        return (int(arr[0]) + 0.0) * int(arr[2])
    elif arr[1] == '/':
        return (int(arr[0]) + 0.0) / int(arr[2])
    
def op1(arr):
    oper_dict = {
    '+':lambda x,y:x+y,
    '-':lambda x,y:x-y,
    '*':lambda x,y:x*y,
    '/':lambda x,y:x/y,
}
    return oper_dict[arr[1]](float(arr[0]),float(arr[2]))

'''将字符串转换成list'''
def replace_op(s):
    s = s.replace('+','|+|')
    s = s.replace('-','|-|')
    s = s.replace('*','|*|')
    s = s.replace('/','|/|')
    return s.split('|')

def split_s(s):
    tmp = ''
    res = []
    for i in s:
        if i in '+-*/':
            res.append(tmp)
            res.append(i)
            tmp = ''
        else:
            tmp += i
    res.append(tmp)
    return res

print split_s(string)
print oper1(replace_op(string),op)