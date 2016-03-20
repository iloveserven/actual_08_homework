list_a = []
list_b = [3,1,4,5,10,2]

#print list_a,list_b

for k in list_b:
    print k

    list_a.append(k)
    for j in range(0,len(list_a)):
        for i in range(0,len(list_a)-1):
            if list_a[i] > list_a[i+1]:
                list_a[i],list_a[i+1] = list_a[i+1],list_a[i]
    

print list_a



'''
list_a.extend(list_b)

for j in range(0,len(list_a)):
    for i in range(0,len(list_a)-1):
        if list_a[i] > list_a[i+1]:
            list_a[i],list_a[i+1] = list_a[i+1],list_a[i]
    
print list_a
'''


