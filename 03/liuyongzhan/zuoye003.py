#coding=utf-8
# encode=utf-8

read_me = '''first of all, i want make it clear that i can not claim undellllllrstddddddddddddanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express ffffffffffffffffffffmy understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

<<<<<<< HEAD
# # 我的做法
# readme_dic={}
# new_readmedic={}
# new_list=[]
# # 统计初始列表中字符出现的次数，生成字典：
# for k in read_me:
#     readme_dic[k] = readme_dic.get(k,0)+1
# # print readme_dic
# # 将字典的键值对调，生成新的字典：
# for key,val in readme_dic.items():
#     if val in new_readmedic:
#         _new_val = new_readmedic[val]
#         if isinstance(_new_val,list):
#             _new_val.append(key)
#         else:
#             new_readmedic[val] = [_new_val,key]
#     else:
#         new_readmedic[val] = key
# # print new_readmedic
# # 将新字典中的键形成一个的列表：
# for k in new_readmedic:
#     new_list.append(k)
# # print new_list
# # 给这个列表从大到小排序,并打印前10：
# count = 1
# while count<11:
# 	# 取出一个最大值，把最大值对应的字符打出来
# 	max_num = max(new_list)
# 	print "第%s名是字符 %s 出现了 %s次 " % (count,','.join(new_readmedic[max_num]),max_num)
# 	# 并列也要算进出现次数
# 	count = count + len(new_readmedic[max_num])
# 	#删除最大值 循环继续
# 	new_list.remove(max_num)


# 老师的第一种方法：
# 统计结果的dict
res = {}
for s in read_me:
	res[s] = res.get(s,0)+1
# dict反转
new_res = {}
for key,val in res.items():
	new_res.setdefault(val,[])
	new_res[val].append(key)
# 取出key
arr = new_res.keys()
count = 0
while count<10:
	# 取出一个最大值，把最大值对应的字符打出来
	max_num = max(arr)
	print "第%s名是字符 %s 出现了 %s次 " % (count+1,'，'.join(new_res[max_num]),max_num)
	# 并列也要算进出现次数
	count = count + len(new_res[max_num])
	#删除最大值 循环继续
	arr.remove(max_num)

# 老师的第二种方法：
# 统计结果的dict
# res = {}
# for s in read_me:
# 	res[s] = res.get(s,0)+1
# # 统计结果变成list,准备排序
# res_list =  res.items()
# # 临时变量，重复出现元素时+1
# count = 0
# # 开始冒泡 提高效率，冒泡过程中就判断是不是并列 打印完直接break 不需要冒泡完全执行
# for i in range(len(res_list)-1):
# 	for j in range(len(res_list)-1-i):
# 		if res_list[j][1]>res_list[j+1][1]:
# 			res_list[j],res_list[j+1] = res_list[j+1],res_list[j]
# 	# 记录当前冒泡结束的最大值和上一个最大值（其实就是右边的一个值）
# 	now_max,pre_max = res_list[-(i+1)],res_list[-i]
# 	# 如果两个相等，记录count
# 	if now_max[1]==pre_max[1]:
# 		count = count+1
# 	else:
# 		# 不相等 count清0
# 		count = 0
# 		if i>10:
# 			break
# 	print '第%s名是字符 %s 出现了 %s次 '%(i+1-count,now_max[0],now_max[1])
# # print res_list
=======
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
>>>>>>> origin/master
