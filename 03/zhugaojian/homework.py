#!/bin/env python

read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''

count_dict = {}
for s in read_me:
    if s in count_dict:
        count_dict[s] += 1
    else:
        count_dict[s] = 1
#print count_dict

v_arr = count_dict.values()
#print v_arr

for j in range(1,len(v_arr)):
    for i in range(j,0,-1):
        if v_arr[i] > v_arr[i-1]:
            v_arr[i],v_arr[i-1] = v_arr[i-1],v_arr[i]
#print v_arr

index_top_10 = 10
for n in range(10,len(v_arr)):
    if v_arr[n-1] > v_arr[n]:
        index_top_10 = n
        break
#print v_arr[:index_top_10]

res_dict = {}
for k,v in count_dict.items():
    if v in v_arr[:index_top_10]:
        if v in res_dict:
            res_dict[v] = res_dict[v]+','+k
        else:
            res_dict[v] = k
#print res_dict
n = 1
tmp = 0
for i in range(index_top_10):
    if tmp != v_arr[i]:
        tmp = v_arr[i]
        print "NO.%s is '%s', occur %s times" %(i+1,res_dict.get(v_arr[i]),v_arr[i])
    n+=1