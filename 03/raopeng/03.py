#!/usr/bin/env python
#coding:utf8
read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
res_dict = {} 
for s in read_me:
    if s in res_dict:
        res_dict[s] = res_dict[s]+1
    else:
        res_dict[s] = 1
####################冒泡排序#################
arr = res_dict.values()
length = len(arr)-1
for j in range(length):
    for i in range(length-j):
        if arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
#print arr
####################字典反转#################
new_dict = {}
for key,val in res_dict.items():
    if val in new_dict:
        new_val = new_dict[val]
        if isinstance(new_val,list):
            new_val.append(key)
        else:
            new_dict[val] = [new_val,key]
    else:
        new_dict[val] = key
#print new_dict
###################比较####################
k = 0 
while k < 10:
    num = arr[k]
    if len(new_dict[num]) == 1:
        print '第%d名%s=======>> %s'%(k+1,new_dict[num],num)
        k += 1
    else:
        for r in new_dict[num]:
            print '第%d名%s=======>> %s'%(k+1,r,num)
            k += 1
#for res in res_dict:
#    print '%s==>%s'%(res,res_dict[res])
#print res_dict

