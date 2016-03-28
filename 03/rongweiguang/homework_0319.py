#!/usr/bin/python

read_me = '''
first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!
'''

ori_dict = {}
res_dict = {}
lst = []

for i in read_me:
        if i in ori_dict:
                ori_dict[i] += 1
        else:
                ori_dict[i] = 1

for key,val in ori_dict.items():
	if val in res_dict:
		res_val = res_dict[val]
		if isinstance(res_val,list):
			res_val.append(key)
		else:
			res_dict[val] = [res_val,key]
	else:
		res_dict[val] = key

for key in res_dict:
	lst.append(key)

for i in range(1,len(lst)):
	for j in range(1,i+1)[::-1]:
		if lst[j] > lst[j-1]:
			lst[j],lst[j-1] = lst[j-1],lst[j]
		else:
			break
for i in range(len(lst[:10])):
	print '"%s" chu xian ci shu di %s duo,\tchu xian le %s ci. '%(','.join(res_dict[lst[:10][i]]),i+1,lst[:10][i])
