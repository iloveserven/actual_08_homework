#coding=utf-8
for i in range(1,10):#到9
    for j in range(1,i+1): #for i in range(1,4):#到9的意思
        print j,"*",i,'=',i*j,"\t",
    print
#方法二
#coding=utf-8
for i in range(1,10):#到9
    s= ''
    for j in range(1,i+1): #for i in range(1,4):#到9的意思
        s = s + str(i)+'*'+str(j)+'='+str(i*j)+'\t'
    print s
#方法三
#coding=utf-8
for i in range(1,10):
   for j in range(1,10):
         if i>=j:
            print '%s * %s =%s' % (i,j,(i*j)),
   print ''






