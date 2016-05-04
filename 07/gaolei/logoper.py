import MySQLdb as mysql
con = mysql.connect(db='gaolei',host='180.153.191.128',user='reboot',passwd='reboot123')
cursor = con.cursor()
def sqloper(sql,ret=None):
    sql = sql
    try:
        cursor.execute(sql)
    except Exception as e:
        return 'error:%s' % e
    else:
        return ret

if __name__ == '__main__':    
    sta = {}
    sta_list = []
    resule_list = []
    with open('log.log') as f:
        for line in f:
            tmp = line.split(' ')
            key = (tmp[0],tmp[8])
            sta[key] = sta.get(key,0)+1
    for key,count in sta.items():
        sta_list.append((key,count))
    for line in sorted(sta_list,key=(lambda x:x[1]),reverse=True)[:100]:
        sql = 'insert into url_sta (ip,status,count) values ("%s",%d,%d)' % (line[0][0],int(line[0][1]),line[1])
        resule_list.append(sqloper(sql,'ok'))
    print resule_list
                      
    

    
