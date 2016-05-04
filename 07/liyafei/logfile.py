#!/usr/bin/python
import sql

def data_file():
  try:
    dt = {}
    with open('www_access_20140823.log') as f:
        while True:
            line = f.readline().split()
            if line:
                ip,status = line[0],line[8]
                dt[(ip,status)] = dt.get((ip,status),0)+1
            else:break
    new_dt = {}
    for key,val in dt.items():
        new_dt.setdefault(val,[])
        new_dt[val].append(key)
    arr = new_dt.keys()
    count = 0
    sql.truncate()
    while count < 100:
        tmp = max(arr)
        ip_tmp, status_tmp, count_tmp = new_dt[tmp][0][0],new_dt[tmp][0][1],tmp
        sql.insert(ip_tmp,status_tmp,count_tmp)
        count +=1
        arr.remove(tmp)
  except:
    return "File not found."
