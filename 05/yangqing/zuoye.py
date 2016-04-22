#!/usr/bin/env python
#-*- coding:utf-8 -*-
def num_list(test):
    numlist = []
    numstr = ""
    re_src = "0123456789+-*/"
    for i in test:
        if i not in re_src:
            continue
        if i in ["+","-","*","/"]:
            numlist.append(numstr)
            numstr = ""
            numlist.append(i)
        else:
            numstr += i
    numlist.append(numstr)
    return numlist
def numsum(numlist):
    num_sum = float(numlist[0])
    for i in range(1,len(numlist),2):
        yunsuan = numlist[i]
        num1 = float(numlist[i+1])
        if yunsuan == "+":
            num_sum += num1
            continue
        if yunsuan == "-":
            num_sum -= num1
            continue
        if yunsuan == "*":
            num_sum *= num1
            continue
        if yunsuan == "/":
            num_sum /= num1
            continue
    return num_sum

str_star = raw_input("input str：")
str_sum = numsum(num_list(str_star))
print str_star ,"==" ,str_sum
