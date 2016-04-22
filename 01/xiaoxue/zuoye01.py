#
ls = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,4112,33,45]

max1=0
max2=0

for i in ls:
    if i > max1:
        max1 = i
    if i > max2 and i < max1:
        max2 = i
print 'Two max numbers is %s and %s . ' %(max1,max2)
