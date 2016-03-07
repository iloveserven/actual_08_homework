a = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,655554,5,777,65555,45,33,45,655554,655554]
c = 0
d = 0
n = 0
for i in a:
    if c < i:
        c = i

for k in a:
    if k == c:
        n += 1
if n != 1:
    print 'the max values is not only one'
    print 'the max values is %s' % c
    print 'the second max values is %s' %c
else:
    for i in a:
        if i == c:
            continue
        if i != c:
            if d < i:
                d = i
    print 'the max values is only one'
    print 'the max values is %s' % c
    print 'the second max values is %s' %d
