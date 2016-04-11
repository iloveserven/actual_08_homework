#encoding=utf-8

f = open('www_access_20140823.log')
ad ={}
for i in f:
	arr = i.split(' ')
	ad[(arr[0],arr[6],arr[8])] = ad.get((arr[0],arr[6],arr[8]),0)+1
#统计IP、路径、状态、次数
res_list = [(k[0],k[1],k[2],v) for k,v in ad.items()]
#生成list
res_str = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
<div class="container">
	<h3>访问数量前十的用户IP、路径、状态</h3>
		<table class='table table-bordered table-striped'>
			<tr colspan="2" style="background-color:#99bbbb;">
				<td>NO.</td>
				<td>IP</td>
				<td>Path</td>
				<td>Status</td>
				<td>Count</td>
			</tr>
'''#定义要输入的内容
tmp = '''
	<tr>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
	</tr>
'''
#定义HTML表格
count = 0
for i in range(len(res_list)-1):
	for j in range(len(res_list)-1-i):
		if res_list[j][3]>res_list[j+1][3]:
			res_list[j],res_list[j+1] = res_list[j+1],res_list[j]	
	now_max,pre_max = res_list[-(i+1)],res_list[-i]
	if now_max[3]==pre_max[3]:
		count = count+1
	else:
		count = 0
	if i >9:
		break
	res_str += tmp % (i+1-count,now_max[0],now_max[1],now_max[2],now_max[3])
#排序取前十，输入到文件内
res_str +='</table>\n</div>'#完成HTML表格标签
f = open('four.html','w') #打开写入到HTML文件
f.write(res_str)
f.close
