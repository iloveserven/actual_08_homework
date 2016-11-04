#!/bin/env python
# coding=utf-8

import requests
import access_log as alog
import mysqldb

db = mysqldb.DB()

res = alog.access_log_list()
for i in res:
    ip = i['ip']
    key = 'q5mTrTGzCSVq5QmGpI9y18Bo'
    url = 'http://api.map.baidu.com/location/ip?ak='+key+'&ip='+ip+'&coor=bd09ll'
    r = requests.get(url).json()
    try:
        geox = r['content']['point']['x']
        geoy = r['content']['point']['y']
        sql = 'update access_log_statistics set geox="%s",geoy="%s" where ip="%s"'%(geox,geoy,ip)
        db.execute(sql)
    except Exception, e:
        print e,r,url