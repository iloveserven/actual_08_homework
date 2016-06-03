
import MySQLdb as mysql
con = None
cursor = None
def connect():
	global con
	global cursor
	con = mysql.connect(db='web',charset='utf8',host='localhost',user='root',passwd='mysql')
	con.autocommit(True)
	cursor = con.cursor()

def execute(sql):
	try:
		cursor.execute(sql)
	except Exception:
		connect()
		cursor.execute(sql)
	return cursor.fetchall()