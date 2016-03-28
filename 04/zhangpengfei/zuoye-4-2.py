# -*- coding: utf-8 -*-

new_dict = {}
new_dict2 = {}

with open('www_access_20140823.log') as  f:
    for rel in  f.readlines():
        arr = []
        arr= (rel.split(' '))
        new_dict[(arr[0],arr[6],arr[8])] = int(new_dict.get((arr[0],arr[6],arr[8]),0)) +1

#字典翻转
for k,v in new_dict.items():
    new_dict2.setdefault(v,[]).append(k)

_html = '''<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet"> <table class="table table-striped">
'''
_str = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
'''
_html = _html + _str%('排名','IP','url','状态','次数')


new_list = new_dict2.keys()
count = 1
while True:
    if count > 10:
        break
    _max = max(new_list)
    for line in new_dict2[_max]:
        _html += _str%(count,line[0],line[1],line[2],_max)
    count = count + len(new_dict2[_max])
    new_list.remove(_max)
_file = open('log.html','w')
_file.write(_html)
_file.close()