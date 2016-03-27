#!/usr/bin/env python
#encoding=utf8
#筛选出所需信息以元组的形式添加至列表，为后面作为字典key做准备
with open('www_access_20140823.log', 'r+') as log_file:
    count_list = []
    for line in log_file.readlines():
        temp = line.split(' \\')[0].split()
        count_list.append((temp[0],temp[6],temp[8],))
# 定义写入文件模型
res_str = '''<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
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
res_str += tmp % ('NO', 'IP', 'url', 'status', 'count')
# 统计记录出现的次数
count_dict = {}
for _tup in count_list:
    count_dict[_tup] = count_dict.get(_tup, 0) + 1
# 冒泡排序,筛选出现次数前十的记录
res_list = count_dict.items()
count = 0
length = len(count_dict) - 1
for x in range(length):
    for y in range(length - x):
        if res_list[y][1] > res_list[y+1][1]:
            res_list[y], res_list[y+1] = res_list[y+1], res_list[y]
    # 记录当前冒泡结束的最大值和上一个最大值
    now_max, pre_max = res_list[-(x+1)], res_list[-x]
    if now_max[1] == pre_max[1]:
        count = count + 1 # 如果相等，记录count次数
    else:
        count = 0 # 如果不相等，清空次数
        if x > 10:
            break
    res_str += tmp % (x+1-count, now_max[0][0], now_max[0][1], now_max[0][2], now_max[1])
    print now_max
res_str += '    </table>'
# 将记录写进文件
with open("access.html", "w+") as acc_cou_file:
    acc_cou_file.write(res_str)
