import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('input')

msg = EmailMessage()
msg['Subject']="hi"
msg['From'] = "phj5996@naver.com"
msg['To'] = "tkdwns6114@naver.com"
# msg.set_content('ssj bs ggggg fuck')
msg.add_alternative('''
<h1>hello</h1>
''', subtype="html")
smtp_url='smtp.naver.com'
smtp_port=465
s = smtplib.SMTP_SSL(smtp_url,smtp_port)
s.login('phj5996',password)
s.send_message(msg)


