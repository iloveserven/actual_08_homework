#coding=utf-8
import smtplib
from email.Header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sendMail(sender,reciver,subject,name):
		smtserver="smtp.sina.com"
		username="yygyihc182@sina.com"
		password="Pass5901"
		msg=MIMEMultipart("alternative")
		msg['Subject']=Header(subject,'utf-8')
		#html格式
		html="""
		<html>
		<head>测试</head>
		<body>
		<p>被删除的账户ID= %s
		</p>
		</body>
		</html> 
		""" % (name)
		htm=MIMEText(html,'html','utf-8')
		msg.attach(htm)
		#构造图片
		# fp=open('mhwl.jpg','rb')
		# msgImage=MIMEImage(fp.read())
		# fp.close()
		# msgImage.add_header("Content-ID", "<image1>")
		# msg.attach(msgImage)
		msg['From']=username
		msg['To']=";".join(reciver)

		#发送邮件
		smtp=smtplib.SMTP()
		smtp.connect(smtserver)
		smtp.login(username, password)
		smtp.sendmail(sender, reciver, msg.as_string())
		smtp.quit()

def autosendmail(name):	
		sender="yygyihc182@sina.com" 
		recivers=['971274269@qq.com']
		subject="嘿，有人删除你的账户，还不去看看"
		try:
			sendMail(sender, recivers, subject,name)
		except Exception,e:
			print str(e)
		return True