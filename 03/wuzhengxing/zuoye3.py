read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
read_d ={}
for k in read_me:
        read_d[k]=read_d.get(k,0)+1
new_dict={}
for key,val in read_d.items():
        if val in new_dict:
                new_val = new_dict[val]
                if isinstance(new_val,list):
                        new_val.append(key)
                else:
                        new_dict[val]=[new_val,key]
        else:
                new_dict[val]=key
list_r=  new_dict.keys()
for i in range(len(list_r)):
        max_a =i
        for n in range(i+1,len(list_r)):
                if list_r[max_a]<list_r[n]:
                        max_a=n
        list_r[i],list_r[max_a]=list_r[max_a],list_r[i]
for i in list_r[:10]:
        print '"%s" chu xian de ci shu shi %s'%(','.join(new_dict[i]),i)
