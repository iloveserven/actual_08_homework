#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Other: suli
# Time: 2016.04.25 10:28
#
# 读取日志
#
import operation_dbs

"""
读取log日志
"""


# 读取日志
def read_log_file(file_name):
    log_source = {}
    with open(file_name, "r") as f:
        count = 0
        while True:
            # sql = "insert into day7.day7_homework (ip, webstatus, num) values(\'%s\',\'%s\', %s)"
            l = f.readline().split()
            if not l:
                break
            tmp = (l[0], l[8])
            log_source[tmp] = log_source.get(tmp, 0) + 1
            # print count
            count += 1

    # log = {}
    # for k, v in log_source.items():
    #     log.setdefault(v, [])
    #     log[v] = k

    return log_source


# 写入数据库
def write_db():

    # count = operation_dbs.execute_mysql("select count(*) from day7.day7_homework")
    # if count[0][0] == 0:
    #     return 0
    log = read_log_file('log.log')
    print len(log)
    for k, v in log.items():
        sql = "insert into day7.day7_homework (ip, webstatus, num) values(\'%s\',\'%s\', %s)"
        sql = sql % (k[0], k[1], v)
        operation_dbs.execute_mysql(sql)


if __name__ == '__main__':
    pass
