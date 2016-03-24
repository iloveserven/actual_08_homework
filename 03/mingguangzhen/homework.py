#!/usr/bin/env python
#encoding=utf8
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
str_dict = {}
for _str in read_me:
    str_dict[_str] = str_dict.get(_str, 0) + 1
count_list = str_dict.items()
# 将count_list表中的元素按照i[1]排序
length = len(count_list)
for x in range(1, length):
    start = 0
    end = x
    while (start <= end):
        mid = (start + end) / 2
        if count_list[x][1] < count_list[mid][1]:
            end = mid - 1
        else:
            start = mid + 1
    if count_list[x][1] == count_list[mid][1]:
        count_list.insert(mid, count_list.pop(x))
    else:
        count_list.insert(start, count_list.pop(x))
# 反转统计好的列表保留前十个最大的元素
count_list_reverse = count_list[-1:-11:-1]
# 遍历统计好的列表查看是否存在并列元素
for i in count_list:
    # 避免重复添加第十个元素
    if (i[1] == count_list_reverse[-1][1]) and (i not in count_list_reverse):
        count_list_reverse.append(i)
for tup in count_list_reverse:
    print "%s ---> %d" % (tup[0], tup[1])
