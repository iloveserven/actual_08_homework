#!/usr/bin/python
read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected!'''

dt = {}
new_dt={}
valnum = []
for i  in read_me:
    dt[i] = dt.get(i,0)+1
for key,val in dt.items():
    if val in new_dt:
        if type(new_dt[val]) != type([]):       
           new_dt[val]  = [new_dt[val],key]
        else:
           new_dt[val].append(key) 
    else:
        new_dt[val] = key 
dt.clear()
valnum = new_dt.keys()
valnum.sort()
valnum.reverse()
t = 1
for n in valnum:
    if valnum.index(n) < 9:
        if type(new_dt[n]) != type([]):
            print 'NO.%d : %s --> %s' %(t,new_dt[n],n)
            t= t+1
        else:
            for i in range(len(new_dt[n])):
                print 'NO.%d : %s --> %s' % (t,new_dt[n][i],n)
            t = t+int(len(new_dt[n]))
