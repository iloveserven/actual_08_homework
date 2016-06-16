#encoding=utf-8
#
import random, string
import requests
import config
import dbutil

def random_str(randomlength=8):
    a = list(string.ascii_letters+'0123456789'+'!@#$%^&*()_+-=')
    random.shuffle(a)
    return ''.join(a[:randomlength])

def log_coll():
    log_addr = 'E:\\Git\\actual_08_homework\\08\\suli\\08.Homework\\log.log'
    handle = {}
    for line in open(log_addr):
        tmp = line.split(' ')
        handle[(tmp[0],tmp[8])] = handle.get((tmp[0],tmp[8]),0) + 1
    return handle

def preserve_log():
    db = dbutil.DB(db=config.db,host=config.db_host,user=config.db_user,passwd=config.db_passwd)
    token = 'CFWb44PtRXTkGqBHlDBRgVG5vGnxnG0a'

    for key,val in log_coll().items():
        if val < 100:
            continue
        url = 'http://api.map.baidu.com/location/ip?ak=%s&ip=%s&coor=bd09ll' % (token,key[0])
        r = requests.get(url)
        
        geo_data = r.json()
        if geo_data['status'] == 0:
            geox = geo_data['content']['point']['x']
            geoy = geo_data['content']['point']['y']
            sql = 'insert into ipmap(ip,status,geox,geoy,count) values("%s","%s","%s","%s","%s")' % (key[0],key[1],geox,geoy,val)
            print 'sql'
            db.execute(sql)
    return True
