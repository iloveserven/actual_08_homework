f=open('www_access_20140823.log','r')
list_n=f.readlines()
f.close()

tmp_lst = []
tmp_dict = {}
new_dict={}
for i in range(len(list_n)):
        tmp_lst = list_n[i].split(' ')[0],list_n[i].split(' ')[6],list_n[i].split(' ')[8]
        tmp_dict[tmp_lst] = tmp_dict.get(tmp_lst,0)+1
#print len(tmp_dict)
for key,val in tmp_dict.items():
        if val in new_dict:
                new_val = new_dict[val]
                if isinstance(new_val,list):
                        new_val.append(key)
                else:
                        new_dict[val]=[new_val,key]
        else:
                new_dict[val]=key
#print new_dict
list_a =  new_dict.keys()
s=len(list_a)
for a in range(s):
        for b in range(1,s-a):
                if list_a[b-1]<list_a[b]:
                        list_a[b],list_a[b-1]=list_a[b-1],list_a[b]
#print list_a
#print new_dict
f=open('/var/www/html/wzx.html','w')
#f.write('<link rel="stylesheet">')
#f.write('\n<p align="center">\nHOMEWORK\n</p>\n')
f.write('<table border="1" align="center" width="800px">\n')
f.write('\n<tr>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n</tr>\n'%('IP','URL','STATUS','COUNT'))
count_1 = 0
while count_1 < 11:
        if isinstance(new_dict[list_a[:10][count_1]],list):
                b=len(new_dict[list_a[:10][count_1]])
                tmp = 10-count_1
                for i in range(b):
                        f.write('\n<tr>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n</tr>\n'%(new_dict[list_a[:10][count_1]][i][0],new_dict[list_a[:10][count_1]][i][1],new_dict[list_a[:10][count_1]][i][2],list_a[:10][count_1]))
                        tmp += 1
                        if tmp>10:
                                break
                count_1 += tmp
        else:
                f.write('\n<tr>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n\t<td>%s</td>\n</tr>\n'%(new_dict[list_a[:10][count_1]][0],new_dict[list_a[:10][count_1]][1],new_dict[list_a[:10][count_1]][2],list_a[:10][count_1]))
                count_1 += 1
f.write('</table>\n')
f.close()
