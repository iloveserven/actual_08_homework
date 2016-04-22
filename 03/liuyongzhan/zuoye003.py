#coding=utf-8
# encode=utf-8

read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

readme_dic={}
new_readmedic={}
new_list=[]
# 统计初始列表中字符出现的次数，生成字典：
for k in read_me:
    readme_dic[k] = readme_dic.get(k,0)+1
# print readme_dic
# 将字典的键值对调，生成新的字典：
for key,val in readme_dic.items():
    if val in new_readmedic:
        _new_val = new_readmedic[val]
        if isinstance(_new_val,list):
            _new_val.append(key)
        else:
            new_readmedic[val] = [_new_val,key]
    else:
        new_readmedic[val] = key
# print new_readmedic
# 将新字典中的键形成一个的列表：
for k in new_readmedic:
    new_list.append(k)
# print new_list
# 给这个列表从大到小排序：
for i in range(len(new_list)-1):
    for j in range(len(new_list)-1-i):
        if new_list[j] < new_list[j+1]:
            new_list[j],new_list[j+1] = new_list[j+1],new_list[j]
# 打印列表中的前十名和它们在新字典中相对应的值：
for x in range(10):
    print "第" , x+1, "名是'%s'，""出现次数为%d次。"%(new_readmedic[new_list[x]],new_list[x])
# 第六名之后是第八