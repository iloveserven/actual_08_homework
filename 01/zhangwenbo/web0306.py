
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
d = {}
max_1 = 0
max_2 = 0

for X in arr:
  if max_1 < X:
     max_1 = X

for Y in arr:
  if Y == max_1:
      continue
  if max_2 < Y:
     max_2 = Y

for Z in arr:
	if Z in d:
		d[Z] = d[Z] + 1
	else:
		d[Z] = 1

if max_1 and max_2  in d:
    print 'max_first is %s and count is %d \nmax_second is %s and count is %d' % (max_1,d[max_1],max_2,d[max_2])