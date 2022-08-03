import datetime as dt
import random
import smtplib 

#**************************   DATE MODULE  *******************************#
now = dt.datetime.now()
send_day = now.weekday()

#**************************   FILE READ MODULE  *******************************#

with open('quotes.txt','r') as file:
    inbound = file.readlines()
    outbound = random.choice(inbound)
    mail_sub = outbound[outbound.index("-") + 2 :]
    mail_body = outbound[0 : outbound.index("-") ]

#**************************   EMAIL MODULE  *******************************#

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "dezynarh@gmail.com"
pas = "Tylenol123"
sms_gateway = 'hazmatlatif@gmail.com'
smtp = "smtp-mail.outlook.com" 
port = 587

def send_mail():  
    with smtplib.SMTP(smtp,port) as server:
        server.starttls()
        server.login(email,pas)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = sms_gateway
        msg['Subject'] = f"A motivation text from {mail_sub}"
        body = mail_body
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        server.sendmail(email,sms_gateway,sms)
    print("Email sent")

if send_day == 1:
    send_mail()