#!/usr/bin/env python
#coding:utf-8

read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''


'''
统计read_me各单词出现的次数
'''
d = {}
for i in read_me:
	if i in d:
		d[i] += 1	
	else:
		d[i] = 1
'''
字典转换成列表，再做冒泡排序
'''
arr = list(d.items())
length = len(arr)-1

for j in range(length):
			for num in range(length-j):
				if arr[num][1]>arr[num+1][1]:
					arr[num],arr[num+1] = arr[num+1],arr[num]


'''
判读最后一个值是否重复，重复就添加
'''

empty_list = []
empty_list = arr[-1:-11:-1]
for i in arr:
	if empty_list[-1][1]==i[1]:
		empty_list.append(i)

'''
格式化打印输出
'''

for num in empty_list:
	print  '%s --> %d' %(num[0],num[1])

