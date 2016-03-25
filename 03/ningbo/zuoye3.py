#!/usr/bin/env python
#coding:utf-8
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''

arr_dict={}
'''  tongji  '''
for i in read_me:
    arr_dict[i]=arr_dict.get(i,0)+1
#print arr_dict
''' dictfanzhuan paixu '''
new_dict={}
for key,val in arr_dict.items():
    if val in new_dict:
        _new_val=new_dict[val]
        if isinstance(_new_val,list):
            _new_val.append(key)
        else:
            new_dict[val]=[_new_val,key]
    else:
        new_dict[val]=key
#print new_dict
#print new_dict.items()
''' liebiaopaixu '''
new_list=new_dict.keys()
new_list.sort()
new_list.reverse()
#print new_list

count=1
for j in new_list:
    while count <=10:
        new_value=new_dict[j]
        if isinstance(new_value,list):
            for length in range(len(new_value)):
                print " 第%d名 : %s 出现 %s 次 " % (count,new_value[length],j)
            count+=len(new_value)
        else:
            print " 第%d名 : %s 出现 %s 次 " % (count,new_value,j)
            count+=1
        break
