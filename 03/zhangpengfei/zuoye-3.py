# -*- coding: utf-8 -*-
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
new_list = []
new_dict = {}
new_dict2 = {}
for i in read_me:
    new_dict[i] = new_dict.get(i,0) + 1
print new_dict
for k,v in new_dict.items():
    if v in new_dict2:
        if isinstance(new_dict2[v],list):
            new_dict2[v].append(k)
        else:
            new_dict2[v] =[new_dict2[v],k]
    else:
        new_dict2[v] = k
print new_dict2
new_arr = new_dict2.keys()
# print new_arr
num = len(new_arr)
# print num
for i in range(num-1):
    for j in range(i+1,num):
        if new_arr[i] < new_arr[j]:
            new_arr[i],new_arr[j] = new_arr[j],new_arr[i]
print new_arr
count = 0
for i in range(10):
    print '第 %s 名 是  "%s"  出现 %d 次'  % (count+1,new_dict2[new_arr[i]],new_arr[i])
    count = count + len(new_dict2[new_arr[i]])
    if count >= 10:
        break




'''
num = len(new_list)
print num
for i in range(num-1):
    for j in range(i+1,num):
        if int(new_list[i][1]) < int(new_list[j][1]):
            new_list[i],new_list[j] = new_list[j],new_list[i]
print new_list
print type(new_list[1][1])
for k in range(num):
    # print k
    if new_list[k][1] == new_list[k+1][1]:
        print 'ss'

'''