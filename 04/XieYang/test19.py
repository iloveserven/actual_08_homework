
f = open('www_access_20140823.log')
count = 0
d={}
tmp = f.readlines()
for i in tmp:
    tmp  = i.split('"')
    tmp[0]=tmp[0].split('-')[0].strip()
    tmp[2]=tmp[2].split('\\')[0].strip()
    merge = '|'.join([tmp[0],tmp[1],tmp[2]])
    if  merge in d:
        d[merge] +=1
    else:
        d[merge] = 1

f.close()
new_res = {}
for key,val in d.items():
    new_res.setdefault(val,[])
    new_res[val].append(key)
arr = new_res.keys()
count = 0
f  = open("aaa.html","w")
mod = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
'''
f.write('''<link href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">\n<table border='1' class="table table-striped">\n''')
f.writelines(mod % ('NUM','IP','URL','STATUS','COUNT'))
while count<10:
    max_num = max(arr)
    if len(new_res[max_num])> 1:
        for i in new_res[max_num]:
            c = i.split('|')
            f.writelines(mod % (count+1,c[0],c[1],c[2],max_num)) 
    else:
        c = new_res[max_num][0].split('|')
        num_1 = c[0]
        num_2 = c[1]
        num_3 = c[2]
        f.writelines(mod % (count+1,c[0],c[1],c[2],max_num))
    arr.remove(max_num)
    count = count + len(new_res[max_num])
f.writelines('</table>')
f.close