#!/usr/bin/env python
#
arr_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

fir_max = 0
sec_max = 0
for fir_num in arr_list:
    if fir_num > fir_max:
        fir_max = fir_num
for sec_num in arr_list:
    if (sec_num > sec_max) and (sec_num < fir_max):
        sec_max = sec_num 
print "The max number is %d" % (fir_max)
print "The second max number is %d" % (sec_max)
