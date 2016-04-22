#!/usr/bin/python

ori_arr =  [3,1,4,5,10,2]
res_arr = []

res_arr.append(ori_arr[-1])

for i in range(len(ori_arr)-1):
        L1 = len(res_arr)
        for j in range(L1):
                if ori_arr[i] > res_arr[j]:
                        res_arr.insert(j,ori_arr[i])
                        break
        L2 = len(res_arr)
        if L1 == L2:
                res_arr.append(ori_arr[i])
print res_arr
