list_aa = []
dict_bb = {}
list_cc = []
f = open('www_access_20140823.log')
n = 0
res_str = '<table border = "1">'
tmp = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
'''
res_str += tmp %('code','url','ip','count')
while True:
    line = f.readline()
    if line == '':
        break
    list_aa = line.split()
    ip = list_aa[0]
    url = list_aa[6]
    code = list_aa[8]

    tuple_cc = (code,url,ip)
    dict_bb[tuple_cc] = dict_bb.get(tuple_cc,0) + 1

#ff = open('sb.txt','w')
#ff.write(dict_bb)

for i in dict_bb:
    code,url,ip = i
    list_cc.append([code,url,(ip,dict_bb.get(i))])

for j in range(10):
    for i in range(len(list_cc)-1):
        if list_cc[i][2][1] > list_cc[i+1][2][1]:
            list_cc[i],list_cc[i+1] = list_cc[i+1],list_cc[i]

for i in list_cc[-1:-11:-1]:
    res_str += tmp %(i[0],i[1],i[2][0],i[2][1])
res_str += '</table>'
ff = open('aaaaaaaaa.html','w')
ff.write(res_str)
ff.close()


    

f.close()
