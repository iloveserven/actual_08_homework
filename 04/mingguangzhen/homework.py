#encoding=utf8
# 筛选log文件中的所有需要的信息，包括：IP、访问状态、访问地址，以元组一组的形式保存到列表中。
#
count_dict = {}
with open("www_access_20140823.log") as log_file:
    for line in log_file.readlines():
        temp = line.split()
<<<<<<< HEAD
        _tup = (temp[0], temp[6], temp[8],)
        count_dict[_tup] = count_dict.get(_tup, 0) + 1
# 反转字典，使用setdefault()
rever_dict = {}
for key,val in count_dict.items():
    rever_dict.setdefault(val, []).append(key)
acc_str = '''<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
=======
        count_list.append((temp[0],temp[6],temp[8],))
# 定义写入文件模型
res_str = '''<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
>>>>>>> origin/master
    <table class="table table-striped">
'''
tmp = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
'''
acc_str += tmp % ('NO','IP','url','status','count')
# 取出字典中所有的key(出现的次数)
key_list = rever_dict.keys()
# 取出最大的key所对应的信息
count = 0
while count < 11:
    max_key = max(key_list)
    key_list.remove(max_key)
    for info in rever_dict[max_key]:
        print info,max_key,count+1
        acc_str += tmp % (count+1,info[0],info[1],info[2],max_key)
    count += len(rever_dict[max_key])
acc_str += '    </table>'
with open('acc_cou.html', 'w+') as acc_file:
    acc_file.write(acc_str)