#coding=utf-8
# 作业
#     实现一个函数，可以做加减乘除
#     不考虑优先级
# oper('1+2*3') == 9
# 不允许用eval

def  oper(tmp):
    arr = ['+','-','*','/']
    temp= ''
    tmplist = list(tmp)
    arr_num = []
    '''正确分割数字与运算符'''
    for i in range(0,len(tmplist)):
        if tmplist[i] not in arr and i < len(tmplist)-1:
            temp = temp + tmplist[i]
        elif i == len(tmplist)-1:
            temp = tmplist[i]
            arr_num.append(int(temp))
        else:
            arr_num.append(int(temp))
            arr_num.append(tmplist[i])
            temp = ''
    '''根据运算府求结果'''
    sum = arr_num[0]
    for i in range(0,len(arr_num)-1) :      
        if arr_num[i] == '+':
            sum = sum+arr_num[i+1]
        elif  arr_num[i] == '-':
            sum = sum-arr_num[i+1]
        elif  arr_num[i] == '*':
            sum = sum*arr_num[i+1]
        elif  arr_num[i] == '/':
            if arr_num[i+1] == 0:
                '''判断分母是否为0'''
                sum = ''
                sum = 'numerror'
                break
            else:
                sum = sum/(arr_num[i+1]+0.0)
        else:
            pass
    print '%s的运算结果为%s' % (tmp,sum)

oper('1+2*3')