#coding=utf-8
read_me =  '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

#新建res_dict字典，将出现的字符及出现次数统计到res_dict中
res_dict = {}   
for s in read_me:
    if s in res_dict:
         res_dict[s] = res_dict[s]+1
    else:
        res_dict[s] = 1
#将res_dict转换成list表
items=res_dict.items()
#将key跟value值对调后，以key值排序
backitems=[[v[1],v[0]] for v in items]
backitems.sort()
#将list中的值反转，打印出前10个
backitems.reverse()
for key,value in backitems[0:10]:
    print value,key
