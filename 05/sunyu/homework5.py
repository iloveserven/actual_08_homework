#-*- coding: utf-8 -*-



#定义加减乘除函数
def js(a,b,s):
    if s == '+':
        return a+b
    elif s == '-':
        return a-b
    elif s == '*':
        return a*b
    elif s == '/':
        return a/b
#str = raw_input('input:')
str = '1+2*3-1/4'
def oper(str):
    str_aa=''
    list_bb = []
    list_cc = []
    total = 0
    for i in str:
        if i == '.':
            continue
        if i == '+' or i == '-' or i == '*' or i == '/':
            i = i
            list_bb.append(i)
        else:
            i = int(i)
            list_bb.append(i)




    while (len(list_bb) > 1):
        for i in list_bb[0:3]:
            list_cc = list_bb[0:3]
            total = js(list_cc[0],list_cc[2],list_cc[1])
 

        list_bb[0:3] = [total]

    print list_bb


oper(str)
