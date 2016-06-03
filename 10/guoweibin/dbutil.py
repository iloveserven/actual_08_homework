import MySQLdb  as mysql

class DB():
	def __init__(self,db,host,user,passwd):
		self.db=db
		self.host=host
		self.user=user
		self.passwd=passwd
		self.connect()

	def  connect(self):
		self.conn=mysql.connect(db=self.db,charset="utf8",host=self.host,user=self.user,passwd=self.passwd)
		self.cursor=self.conn.cursor()
		self.conn.autocommit(True)
	def execute(self,sql):
		print sql
		try:
			self.cursor.execute(sql)
		except  Exception,e:
			print e 
			try:
				self.conn.close()
				self.cursor.close()
			except:
				pass

			
			self.connect()
			self.cursor.execute(sql)
		res=self.cursor.fetchall()
		print res
		return res

		# return self.cursor.fetchall()







# conn= None
# cursor = None
# def connect():
#                global  conn
#                global   cursor
#                conn=mysql.connect(db='guoweibin',host='localhost',user='root',passwd='123456')
#                conn.autocommit(True)
#                cursor=conn.cursor()
   
   
# def  execute(sql):
# 	try:
# 		cursor.execute(sql)
# 	except Exception:
# 		print  'connect db'
# 		connect()
# 		cursor.execute(sql)
# 	return cursor.fetchall()

     

