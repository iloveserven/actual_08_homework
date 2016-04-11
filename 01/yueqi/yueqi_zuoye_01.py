#! /usr/bin/python
list_A=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
dict_A={}
first_num=0
second_num=0
for i in list_A:
        if i not in dict_A:
                dict_A[i]=0
        dict_A[i]=dict_A[i]+1
for j in list_A:
        if j > first_num:
                first_num=j
for z in list_A:
        if z==first_num and dict_A[z]==1:
                continue
        elif z > second_num and dict_A[z]>=1:
                second_num=z
print 'First num: %s Second num: %s' %(first_num,second_num)
