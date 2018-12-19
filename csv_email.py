import csv
import smtplib
from email.message import EmailMessage
import getpass

password = getpass.getpass('input')

f = open('pygj.csv','r',encoding='utf-8')

read_csv = csv.reader(f)
smtp_url='smtp.naver.com'
smtp_port=465
s = smtplib.SMTP_SSL(smtp_url,smtp_port)
s.login('phj5996',password)
for line in read_csv:
    msg = EmailMessage()
    msg['Subject']="안녕하세요"
    msg['From'] = "phj5996@naver.com"
    msg['To'] = line[1]
    msg.set_content(line[0]+'에게 보냄')
    s.send_message(msg)
  
    
f.close()
