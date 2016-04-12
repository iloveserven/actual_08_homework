#-*- coding: utf-8 -*-

##定义数字和符合集合
numberable=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
signs = ["+", "-", "*", "/"]

##返回表达式的最后一个元素
def getLast(l):
    if l:
        return l[len(l)-1]

##解析表达式
def parse_function(_str):
        result=[]
        cur=""
        for index in range(len(_str)):
            ch=_str[index]
            if ch in numberable:
                cur+=ch
            elif ch in signs:
                if cur:
                    result.append(float(cur))
                    cur=""
                if ch in ["*","/"] and getLast(result)==ch:
                    result[len(result)-1]*=2
                elif ch in ["+","-"] and getLast(result) in signs and _str[index+1] not in signs:
                    cur+=ch
                else:
                    result.append(ch)
            else:
                raise Exception,"Error"
        if cur:
            result.append(float(cur))
        return result


##将表达式按照符号优先级合并
def changeExpression(arr):
    while "*" in arr or "/" in arr:
        for i in range(len(arr)):
            if arr[i]=="*" or arr[i]=="/":
                tmp=[arr[i-1],arr[i],arr[i+1]]
                arr[i-1]=tmp
                del arr[i]
                del arr[i]
                break
    return  arr

##定义常用的几种计算表达式
def cals(a,b,sign):
    if sign=="+":
        return a+b
    elif sign=="-":
        return a-b
    elif sign=="*":
        return a*b
    elif sign=="/":
        return a/b
    else:
        raise Exception("Unsupport sign: %s" %sign)

##进行表达式计算
def lastcals(arr):
    result=0.0
    if len(arr)==1:
        if type(arr[0])!=type([]):
            return float(arr[0])
        else:
            return lastcals(arr[0])
    else:
        return cals(lastcals(arr[:len(arr)-2]),lastcals([arr[-1]]),arr[-2])

print lastcals(changeExpression(parse_function('1+2*3-11/2+7+2*3')))







