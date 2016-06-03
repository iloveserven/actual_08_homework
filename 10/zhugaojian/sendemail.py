# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

class SendMail(object):
    def __init__(self, subject,msg,to):
        self.subject = subject
        self.msg = msg
        self.to = to


    def _format_addr(self,s):
        name,addr = parseaddr(s)
        return formataddr((Header(name,'utf-8').encode(),addr.encode('utf-8') if isinstance(addr,unicode) else addr))

    def send_mail(self):
        from_addr = 'zhugaojianreboot@sina.com'
        password = 'gaojian_reboot'
        smtp_server = 'smtp.sina.com'

        mailmsg = MIMEText(self.msg,'plain','utf-8')
        mailmsg['From'] = self._format_addr(u'zhugaojian<%s>' % from_addr)
        mailmsg['To'] = self._format_addr(self.to)
        mailmsg['Subject'] = Header(self.subject,'utf-8').encode()

        server = smtplib.SMTP(smtp_server,25)
        # server.set_debuglevel(1)
        server.login(from_addr,password)
        server.sendmail(from_addr,[self.to],mailmsg.as_string())
        server.quit()

# m = SendMail('test mail','test mail content','zhugaojian<zhugaojian@sina.com>')
# m.send_mail()