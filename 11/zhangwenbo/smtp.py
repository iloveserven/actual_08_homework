#coding=utf-8
import smtplib
from email.Header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sendMail(sender,reciver,subject,user_id):
		smtserver="smtp.sina.com"
		username="********@sina.com"
		password="*****"
		msg=MIMEMultipart("alternative")
		msg['Subject']=Header(subject,'utf-8')
		#html格式
		html="""
		<html>
		<body>
		<p>被删除的账户ID= %s
		</p>
		</body>
		</html> 
		""" % (user_id)
		htm=MIMEText(html,'html','utf-8')
		msg.attach(htm)
		msg['From']=username
		msg['To']=";".join(reciver)

		#发送邮件
		smtp=smtplib.SMTP()
		smtp.connect(smtserver)
		smtp.login(username, password)
		smtp.sendmail(sender, reciver, msg.as_string())
		smtp.quit()

def autosendmail(user_id):	
		sender="*******@sina.com" 
		recivers=['***********@qq.com']
		subject="嘿，有人删除你的账户，还不去看看"
		try:
			sendMail(sender, recivers, subject,user_id)
		except Exception,e:
			print str(e)
		return True