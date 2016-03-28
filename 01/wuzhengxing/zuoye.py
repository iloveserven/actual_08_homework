#!/usr/bin/python
lis_nu= [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
dict_nu ={}
for a in lis_nu:
        if a in dict_nu:
                dict_nu[a] = dict_nu[a]+1
        else:
                dict_nu[a] =1
max_nu = lis_nu[0]
sec_nu = lis_nu[0]
for n in lis_nu:
        if n>max_nu:
                max_nu = n
if dict_nu[max_nu]!=1:
        sec_nu=max_nu
        print 'max mun is %s'%(max_nu)
        print 'second num is %s'%(sec_nu)
else:
        for i in lis_nu:
                if max_nu>i and sec_nu<i:
                        sec_nu  =i
        print 'max mun is %s'%(max_nu)
        print 'second num is %s'%(sec_nu)
