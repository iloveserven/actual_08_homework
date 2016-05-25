#/usr/bin/python
f = open('www_access_20140823.log')
dt = {}
while True:
    line = f.readline().split()
    if line:
        tmp_tp = (line[0],line[6],line[8])
        dt[tmp_tp] = dt.get(tmp_tp,0)+1
    else:break
f.close()
new_dt = {}
for key,val in dt.items():
    new_dt.setdefault(val,[])
    new_dt[val].append(key)
res = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
'''
f = open('xcc.html','a+')
f.write("<table border='1'>")
f.write(res % ('NO','IP','Path','Status','Count'))
arr = new_dt.keys()
count = 1

while count < 10:
    max_num = max(arr)
    if len(new_dt[max_num]) == 1:
        f.write(res % (count,new_dt[max_num][0][0],new_dt[max_num][0][1],new_dt[max_num][0][2],max_num))
        count += 1
        arr.remove(max_num)
    else:
        for key in range(len(new_dt[max_num])):
            f.write(res % (count,new_dt[max_num][key][0],new_dt[max_num][key][1],new_dt[max_num][key][2],max_num))
        count = count + len(new_dt[max_num])
        arr.remove(max_num)
f.write('\n</table>')
f.close()
