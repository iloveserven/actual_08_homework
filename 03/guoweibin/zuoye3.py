# -*- coding: utf-8 -*-
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
#统计每个字符的出现的次数
dict_read={}
for key in read_me:
    dict_read[key]=dict_read.get(key,0)+1
# print dict_read

#对字典的key和value进行反转，形成新的字典new_dict
new_dict={}
for key,val in dict_read.items():
    if val not in new_dict:
        new_dict[val]=key
    elif val in new_dict:
        if type(new_dict[val])!=type([]):
            new_dict[val]=[new_dict[val],key]
        else:
            list_value=new_dict[val]
            list_value.append(key)
# print new_dict

#将形成的字典new_dict转成list
list_read=[]
for key in new_dict:
    list_read.append([key,new_dict[key]])
# print list_read

#对形成的list进行排序
for i in range(len(list_read)):
    for j in range(1,i+1)[::-1]:
        if list_read[j][0]<list_read[j-1][0]:
            list_read[j],list_read[j-1]=list_read[j-1],list_read[j]
        else:
            break
# print list_read

#输出最大的十个字符
length=len(list_read)
for i in range(length-1,length-11,-1):
    print "出现第" , length-i,"多的字符为：" , list_read[i][1], "出现：" , list_read[i][0], ' 次'


#########################################################################
# 字典反转后的，另一种方法解决方法：
#对新字典按照key值排序,形成list
list_read=new_dict.items()
#对list使用sort函数排序
list_read.sort()
length=len(list_read)
#打印输出出现次数最多的10个字符
for i in range(length-1,length-11,-1):
    print "出现第",length-i,"多的字符为：",list_read[i][1],"出现：",list_read[i][0],' 次'





