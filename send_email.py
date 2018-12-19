import smtplib
from email.message import EmailMessage
import getpass

password = getpass.getpass('input')

email_list =['tkdwns6114@naver.com','domw324@gmail.com']

for e in email_list:
    msg = EmailMessage()
    msg['Subject']="hi"
    msg['From'] = "phj5996@naver.com"
    msg['To'] = e
    msg.set_content('ssj bs ggggg fuck')
    smtp_url='smtp.naver.com'
    smtp_port=465
    s = smtplib.SMTP_SSL(smtp_url,smtp_port)
    s.login('phj5996',password)
    s.send_message(msg)
    

