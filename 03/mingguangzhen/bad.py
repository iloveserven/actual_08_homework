#!/usr/bin/env python
#encoding=utf8
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''
# 循环文本，将每个字符出现的次数统计至字典中
new_dict = {}
for _str in read_me:
    new_dict[_str] = new_dict.get(_str, 0) + 1
reverse_dict = {}
# 统计字符数量，存入reverse_dict中
for _key,_val in new_dict.items():
    if reverse_dict.has_key(_val):
        if isinstance(reverse_dict[_val], list):
            reverse_dict[_val].append(_key)
        else:
            reverse_dict[_val] = [reverse_dict[_val], _key]
    else:
        reverse_dict[_val] = _key
# 取出所有字符出现的数量存入列表，并降序
key_list = reverse_dict.keys()
key_list.sort()
key_list.reverse()
# 循环列表取出字典中对应的值
cout = 0
for num in key_list:
    # 判断字典中的值是否为列表
    if isinstance(reverse_dict[num], list):
        # 循环列表中的值打印出来，计算前十cout
        cout_tem = cout + 1
        for tem in reverse_dict[num]:
            cout += 1
            print "NO.%d:'%s' ---> %d times" % (cout_tem, tem, num)
        if cout >= 10:
            break
    else:
        cout += 1
        print "NO.%d:'%s' ---> %d times" % (cout, reverse_dict[num], num)
        if cout >= 10:
            break
