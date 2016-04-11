# -*- coding: utf-8 -*-
arr = '11+24*15/3*4-3+116+6669-37/5'

def cal(term01,term02,n):
    if n =='+':
        return term01+term02
    elif n == '-':
        return term01-term02
    elif n== '*':
        return term01*term02
    elif n == '/':
        return term01/term02

#将arr变成['11', '+', '24', '*', '15', '/', '3', '*', '4', '-', '3', '+', '116', '+', '6669', '-', '37', '/', '5']    
def change(L):
    tmp_L = L.replace('+',' + ')
    tmp_L = tmp_L.replace('-',' - ')
    tmp_L = tmp_L.replace('*',' * ')
    tmp_L = tmp_L.replace('/',' / ')
    return tmp_L.split( )
#再变成['11', '+', [[['24', '*', '15'], '/', '3'], '*', '4'], '-', '3', '+', '116', '+', '6669', '-', ['37', '/', '5']]
def advChange(arr):
#    arr = arr[:]
    while '*' in arr or '/' in arr:
        for i in range(len(arr)):
            if arr[i] == '*' or arr[i] == '/':
                tmparr = [arr[i-1],arr[i],arr[i+1]]
                arr[i-1] = tmparr
                del arr[i]
                del arr[i]
                break
    return arr
#进行运算
def langCal(arr):
    if len(arr) == 1:
        if not isinstance(arr[0],list):
            return int(arr[0])
        else:
            return langCal(arr[0])
    else:
        return cal(langCal(arr[:len(arr)-2]),langCal([arr[-1]]),arr[-2])
#进行结合，如果不调用advChange()，则无优先级
def fina(L):
    tmp_arr = change(L)
#    print tmp_arr
    tmp_arr = advChange(tmp_arr)
#    print tmp_arr
    return langCal(tmp_arr)

ret = fina(arr)
print ret
