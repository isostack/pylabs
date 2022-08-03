##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import random
import datetime as dt
date_now = dt.datetime.now()
now_month = date_now.month
celebrator = None
content = None

def make_mail():
    global content
    filr = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filr,'r') as file:
        inbound = file.read()
        content = inbound.replace("[NAME]",celebrator)
        
    send_mail()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "dezynarh@gmail.com"
pas = "Tylenol123"
mail_gateway = "hazmatlatif@gmail.com"
smtp = "smtp-mail.outlook.com"
port = 587

def send_mail():  
    with smtplib.SMTP(smtp,port) as server:
        server.starttls()
        server.login(email,pas)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = mail_gateway
        msg['Subject'] = f"Happy Birthday!"
        body = content
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        server.sendmail(email,mail_gateway,sms)
    print("Email sent")

import pandas 
birthdays = pandas.read_csv("birthdays.csv")

for index,row in birthdays.iterrows():
    if row["month"] == now_month:
        celebrator = row["name"]
        make_mail()
    else:
        pass






