#/usr/bin/env python
#-*- coding:utf-8 -*-
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
res_dict = {}
#统计字符数量
for i in read_me:
	res_dict[i] = res_dict.get(i,0)+1
#反转数量与对应字符，生成新dict
new_res = {}
for key,val in res_dict.items():
	new_res.setdefault(val,[])
	new_res[val].append(key)
key_arr = new_res.keys()
count = 1
while count < 11:
	max_count = max(key_arr)
	print count,max_count,new_res[max_count]
	key_arr.remove(max_count)
	count = count + len(new_res[max_count])

