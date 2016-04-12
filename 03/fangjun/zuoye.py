#!/usr/bin/python27
#encoding=utf-8
#统计字符串中每个字符出现的个数，并取出字符出现次数最多的前10个字符
#总体思路：遍历字符串，将字符作为键，出现的次数作为值存入一个字典中; 取出字典中所有键的值存放一个列表中，再对对列表进行排序。遍历列表中最后10个数值最大的元素,再遍历字典，如果字典中某个键的值等于所遍历列表中的值，将这个字典的键值存入一个字典中，当前字典的长度等于10时，结束循环，最后再打印结果。
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''

str_dict = {}
for s in read_me:
    str_dict[s] = str_dict.get(s,0) + 1     #将字符作为键，字符所出现的次数作为值存放字典str_dict中

# print str_dict

new_dict = {}           #定义一个字典，用于存放出现次数Top10的字符
vList = str_dict.values() #取出字典所有键的值，并存入vList这个列表中

#使用插入排序对vList进行排序
for i in range(1,len(vList)):
    for j in range(i,0,-1):
        if vList[j] < vList[j-1]:
            vList[j],vList[j-1] = vList[j-1],vList[j]

for i in range(len(vList)-1,len(vList)-11,-1):   #外循环：从后向前遍历列表vList十次,取出列表最后10个最大的值
    for k in str_dict:                           #内循环：遍历字典
        if ( str_dict[k] == vList[i] ) and ( k not in new_dict ):  #判断字典键为k的值是否和列表中下标为i的值相等,并且这键k不在new_dict中
            new_dict[k] = str_dict[k]            #把str_dict的键和它对应的值赋new_dict这个字典
            if len(new_dict) == 10:   #判断new_dict的长度是否为10,若不判断,当字典new_dict的长度大于10，还会继续添加值相同的键,new_dict的长度会大于10
                break                            #若长度为10，则跳出内循环不再遍历字典    
print '-'*20,"Top10:",'-'*20,'\n'
print new_dict          #打印出现次数top10的字符及出现的次数
# 没考虑并列