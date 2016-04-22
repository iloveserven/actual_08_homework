#!/usr/bin/env python
read_str = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
dict_list = {}

for i in read_str:
    dict_list[i] = dict_list.get(i,0)+1


new_dict = {}
for key,val in dict_list.items():
    if val in new_dict:
        _new_value = new_dict.get(val)
        if isinstance(_new_value,list):
            new_dict[val].append(key)
        else:
            new_dict[val] = [_new_value,key]
    else:
        new_dict[val] = key
print new_dict

new_list = []
for i in  new_dict:
    new_list.append(i)
for i in range(len(new_list)-1):
    for j in range(len(new_list)-i-1):
        if new_list[j] > new_list[j+1]:
            new_list[j],new_list[j+1] = new_list[j+1],new_list[j]

print new_list
a = len(new_list)

for i in range(a-1,a-10,-1):
    if type([]) == type(new_dict[new_list[i]]):
        for j in range(len(new_dict[new_list[i]])):
            print i,new_dict[new_list[i]][j]
            print "xxx"
        i = i - len(new_dict[new_list[i]])
    print  i,new_dict[new_list[i]]
