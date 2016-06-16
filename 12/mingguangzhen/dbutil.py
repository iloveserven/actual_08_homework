#encoding=utf-8

import MySQLdb as mysql

class DB():
    def __init__(self,db,host,user,passwd):
        self.db = db
        self.host = host
        self.user = user
        self.passwd = passwd
        self.connect()
    def connect(self):
        self.con = mysql.connect(db=self.db,charset='utf8',host=self.host,user=self.user,passwd=self.passwd)
        self.cursor = self.con.cursor()
        self.con.autocommit(True)
    def execute(self,sql):
        print sql
        try:
            self.cursor.execute(sql)
        except Exception, err:
            print err
            try:
                self.con.close()
                self.cursor.close()
            except Exception, e:
                pass
            self.connect()
            self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print res
        return res

# con = None
# cursor = None
# def connect():
#     global con 
#     global cursor
#     con = mysql.connect(db='mingguangzhen', charset='utf8' host='180.153.191.128', user='reboot', passwd='reboot123')
#     con.autocommit(True)
#     cursor = con.cursor()

# def execute(sql):
#     try:
#         cursor.execute(sql)
#     except Exception, err:
#         #print err
#         try:
#             cursor.close()
#             con.close()
#         except Exception as e:
#             pass
#         print 'con db again.'
#         connect()
#         cursor.execute(sql)
#     return cursor.fetchall()

# def log_info(start,cont):
#     sql = 'select * from log_data limit %s,%s' % (start,cont)
#     return execute(sql)




# '''
# For user management.
# Support add/del/modified/select
# '''

# def user_info():
#     sql = 'select id,username,password from user'
#     return execute(sql)

# def auth_info():
    # info_dict = {}
    # sql = 'select username,password from user'
    # res_list = execute(sql)
    # for tup in res_list:
    #     info_dict[tup[0]] = tup[1]
    # return info_dict

# def ins_user(user,pwd):
#     sql = 'insert into user(username,password) values("%s","%s")' % (user,pwd)
#     execute(sql)
#     return True

# def del_user(id):
#     sql = 'delete from user where id=%s' % (id)
#     execute(sql)
#     return True

# def update_user(uppwd,id):
#     sql = 'update user set password="%s" where id=%s' % (uppwd,id)
#     # print sql
#     execute(sql)
#     return True


# '''
# For resource management.
# Support add/del/modified/select
# '''
# def res_info():
#     sql = 'select * from res_mgt'
#     return execute(sql)

# def ins_res(host_name,cpu_core,mem_size,val_per,contacts):
#     sql = 'insert into res_mgt(host_name,cpu_core,mem_size,val_per,contacts) values("%s","%s","%s","%s","%s")' % (host_name,cpu_core,mem_size,val_per,contacts)
#     execute(sql)
#     return True

# def del_res(id):
#     sql = 'delete from res_mgt where id=%s' % (id)
#     execute(sql)
#     return True

# def update_res(res_dict):
#     sql = 'update res_mgt set host_name="%s",cpu_core="%s",mem_size="%s",val_per="%s",contacts="%s" where id=%s' % (res_dict['host_name'],res_dict['cpu_core'],res_dict['mem_size'],res_dict['val_per'],res_dict['contacts'],res_dict['userid'])
#     execute(sql)
#     return True
