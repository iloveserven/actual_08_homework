#coding=utf-8
num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_1 = 0
max_2 =0
for qqq in num_list:
    if max_1 < qqq:
        max_1 = qqq
print max_1

for qqq in num_list:
    if qqq == max_1:
        continue
    else:
        if max_2 <qqq:
            max_2 =qqq
print max_2