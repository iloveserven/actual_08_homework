# -*- coding: utf-8 -*-
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
#统计每个字符的出现的次数
dict_read={}
for key in read_me:
    dict_read[key]=dict_read.get(key,0)+1
print dict_read

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
print new_dict

##输出前十的元素
count=1
key_arr=new_dict.keys()
while count<11:
    max_count=max(key_arr)
    print "第 %s名，字符为：%s, 出现次数为：%s"%(count,new_dict[max_count],max_count)
    key_arr.remove(max_count)
    count=count+len(new_dict[max_count])







