#!/usr/bin/python

list_ss = []
num=''

while True:
        num = raw_input('please input num:')
        if num == 'qq':
                break
        l_1=len(list_ss)
        for n in range(l_1):
                if int(num) > list_ss[n]:
                        list_ss.insert(n,int(num))
                        break
        l_2=len(list_ss)
        if l_1==l_2:
                list_ss.append(int(num))
print list_ss
