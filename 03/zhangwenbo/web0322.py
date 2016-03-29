#coding=utf-8

read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

read_dict = {}
for s in read_me:
	read_dict[s] = read_dict.get(s,0)+1
#统计字符
list_new = read_dict.items()
list_new_d =sorted(list_new,key=lambda x:x[1],reverse=True)[:10]
#排序取前十
count = 0
for i in range(len(list_new_d)-1):
	if list_new_d[i][1] == list_new_d[i-1][1]:
		count = count +1
	else:
		count = 0
		if i > 10:#满足值相等且循环十次就break，不在往下执行
			break
	print "%s  character: '%s' , count: %s" % (i+1-count,list_new_d[i][0],list_new_d[i][1])
#打印前十，按照统计次数排序，并列排名打印出来

