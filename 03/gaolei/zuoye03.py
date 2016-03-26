# -*- coding: utf8 -*-
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

dic = {} 
r_dic = {} 
times = 0 #记录输出多少字符
for i in read_me:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1


for itm,cot in dic.items():
    if cot in r_dic:
        r_dic[cot].append(itm)
    else:
        r_dic[cot] = [itm]

arr = r_dic.keys()
print arr
while True:
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    print "The NO.%d character is '%s',and the number is %d" % (times+1,','.join(r_dic[arr[max_index]]),arr[max_index])
    times = times + len(r_dic[arr[max_index]])
    del arr[max_index]
    if times >= 10: #计算上一次打印后的字符有没有超过10，没有就打印下一个。
        break


