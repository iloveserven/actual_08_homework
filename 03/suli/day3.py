#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# created sllzwsgdsg 
# github: https://github.com/sllzwsgdsg 
# 统计字符串内单个字符出现的次数, 根据次数进行排序, 得到前N名

note = """first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!"""


# 统计字符串内字符的数量
def note_count_func(note):
	note_count = {}
	for i in note:
		note_count[i] = note_count.get(i, 0) + 1

	return note_count


# 对统计好的字典进行拆分,排序
def sort_note_sub(note_count):
	sort_note_k = [] # keys
	sort_note_v = [] # values

	# 拆分key 和 value
	for k, v in note_count.items():
		sort_note_k.append(k)
		sort_note_v.append(v)

	# 开始排序
	n = len(sort_note_v)
	for i in range(n):
		for j in range(1, n-i):
			if sort_note_v[j] > sort_note_v[j-1]:
				# 同时排序key 和 values 的 list
				sort_note_k[j-1], sort_note_k[j] = sort_note_k[j], sort_note_k[j-1]
				sort_note_v[j-1], sort_note_v[j] = sort_note_v[j], sort_note_v[j-1]

	# 返回keys, values
	return sort_note_k, sort_note_v


# 显示排行榜, 参数: 显示数量
def show_rank(max):
	k,v = sort_note_sub(note_count_func(note))
	print "=====       前%s名:       =====" % max
	for i in range(max):
		print "第%2d名: (字符:%s, 出现次数: %s)" % (i+1, k[i], v[i])


# ==============================================
# ==============================================
if __name__ == "__main__":
	# 参数: 显示前N名
	show_rank(15)

