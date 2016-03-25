#!/usr/bin/python27
#encoding=utf-8
#统计字符串中每个字符出现的个数，并取出字符出现次数最多的前10个字符
#TOp10思路：将字典转换成一个二维数组，再对二维数组按字符的次数进行排序。
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''

str_dict = {}
for s in read_me:
    str_dict[s] = str_dict.get(s,0) + 1

#把字典的键值存放到一个二维数组中
strList = []
for k,v in str_dict.items():
    strList.append([k,v])

#对strList列表进行冒泡排序
"""
for j in range(0,len(strList)-1):
    for i in range(0,len(strList)-1):
        if strList[i][1] > strList[i+1][1]:
            strList[i],strList[i+1] = strList[i+1],strList[i]
"""

#对strList进行插入排序
for i in range(1,len(strList)):
    for j in range(i,0,-1):
        if strList[j][1] < strList[j-1][1]:
            strList[j],strList[j-1] = strList[j-1],strList[j]

#取出strList中的最后10个元素，即Top10
print strList
print "-"*60,"Top 10","-"*60
count = 0
for i in range(len(strList)-1,len(strList)-11,-1):
    print "第%d名的字符是：%s,出现次数是：%d" %(count+1,strList[i][0],strList[i][1])


