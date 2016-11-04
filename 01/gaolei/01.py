#!/usr/bin/python
numlist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
fir = 1  
sec = fir
for i in numlist:
  if i >= fir:
    sec = fir
    fir = i
  elif i > sec:
    sec = i
print 'the largest number is %d,the second largest number is %d' % (fir,sec)

