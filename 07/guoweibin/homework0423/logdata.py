import MySQLdb  as mysql

conn=mysql.connect(db='guoweibin',host='localhost',user='root',passwd='123456')
conn.autocommit(True)
cursor=conn.cursor()

def  logacess(filename):
	res={}

        with open(filename) as f:
              for line in f:
                      tmp=line.split(' ')
                      user_ip,user_state=tmp[0],tmp[8]
                      res[(user_ip,user_state)]=res.get((user_ip,user_state),0)+1

                  

              new_dict={}
              for key,val in  res.items():
    	              new_dict.setdefault(val,[])
    	              new_dict[val].append(key)

              arr =new_dict.keys()
              count=0
              cursor.execute('truncate table logdb')
              sql=  'insert into logdb (user_ip,user_state,ip_number) values  ("%s","%s","%s")'

              while count<100:
    	              max_count  =  max(arr)
    	              tmp=new_dict[max_count]
    	              for  tup in new_dict[max_count]:
    	              	      cursor.execute(sql%(tup[0],tup[1],max_count))
    	              count=count+len(new_dict[max_count])
    	              arr.remove(max_count)
        







