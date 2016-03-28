#! /usr/bin/python
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
dict_read_me={}
dict_read_new={}
list_read_new=[]
for i in read_me:
	dict_read_me[i]=dict_read_me.get(i,0)+1
for key,val in dict_read_me.items():
	if val in dict_read_new:
		if isinstance(dict_read_new[val],list):
			dict_read_new[val].append(key)
		else:
			dict_read_new[val]=[dict_read_new[val],key]
	else:
		dict_read_new[val]=key
list_read_new=dict_read_new.items()
for i in range(0,len(dict_read_new)-1):
	for j in range(i,len(dict_read_new)):
		if list_read_new[i][0]<list_read_new[j][0]:
			list_read_new[i],list_read_new[j]=list_read_new[j],list_read_new[i]
for m in range(0,10):
	print m+1 , list_read_new[m]
