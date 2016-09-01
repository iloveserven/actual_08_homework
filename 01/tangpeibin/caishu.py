#coding=utf-8
import random
n = random.randint(1,10)
count=0
while True:
    count = count+1
    if count ==4:
        print "输入超过3次，这个数是",n
        break
    shu =int(raw_input('please input enter'))
    if n==shu:
        print "6666"
    elif shu <n:
        print "你输入小了"
    elif shu >n:
        print "你输入大了"