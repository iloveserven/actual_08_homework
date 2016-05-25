#!/usr/bin/env python
#encoding=utf8
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
res_dict = {}
for _str in read_me:
    res_dict[_str] = res_dict.get(_str, 0) + 1
res_list =res_dict.items()
length = len(res_list)-1
count = 0
for i in range(length):
    for j in range(length-i):
        if res_list[j][1] > res_list[j+1][1]:
            res_list[j], res_list[j+1] = res_list[j+1], res_list[j]
            
    now_max, pre_max = res_list[-(i+1)], res_list[-i]
    if now_max[1] == pre_max[1]:
        count += 1
    else:
        count = 0
        if i > 10:
            break
    print "第%s名，字符是%s,出现了%s次" % (i+1-count, now_max[0], now_max[1])
