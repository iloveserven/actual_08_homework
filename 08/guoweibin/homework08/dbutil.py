import MySQLdb  as mysql

conn= None
cursor = None
def connect():
               global  conn
               global   cursor
               conn=mysql.connect(db='guoweibin',host='localhost',user='root',passwd='123456')
               conn.autocommit(True)
               cursor=conn.cursor()
   
   
def  execute(sql):
	try:
		cursor.execute(sql)
	except Exception:
		print  'connect db'
		connect()
		cursor.execute(sql)
	return cursor.fetchall()

     

