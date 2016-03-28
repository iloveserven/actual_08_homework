#coding:utf8

#定义一个空字典，存放IP,访问路径,状态 出现次数。
dict = {}
#打开本地目录下的文件，剔除左右两边空白符号，以换行符进行切割。
with open('www_access_20140823.log') as f:
    for line in f.read().strip().split('\n'):
        L = line.split()
        dict[(L[0],L[6],L[8])] = dict.get((L[0],L[6],L[8]),0) + 1
#将字典item成元组元素的列表。
res_list = dict.items()
#冒泡排序,将html的表单数据字符添加至tmp变量。
length = len(res_list) - 1
count = 0
tmp = ''
for i in xrange(length):
    for j in xrange(length - i):
        #print length
        if res_list[j][1] > res_list[j+1][1]:
            temp = res_list[j]
            res_list[j] = res_list[j+1]
            res_list[j+1] = temp 
    now_max,pre_max = res_list[-(i+1)],res_list[-i]
    if now_max[1] == pre_max[1]:
        count = count + 1
    else:
        count = 0
        if i > 10:
            break
    tmp += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (i+1-count,','.join(now_max[0]),now_max[1])

#定义html内容,表单数据使用tmp变量。
stat_html_content = '''

<head>
	<link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
	<script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
	<script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
</head>
<body>
<h1 style="text-align:center">日志数据统计表</h1>
<table class="table table-bordered">
    <th>
        <tr><td>序号</td><td>访问内容</td><td>访问次数</td></tr>
    </th>
    <tbody>
        %s
    </tbody>
</table>
</body>
'''  % tmp

#将html内容写入本地static.html文件。
with open('stat.html','w') as static_html:
    static_html.write(stat_html_content)



