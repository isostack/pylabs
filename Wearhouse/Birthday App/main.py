##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import random
import datetime as dt
import json

inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

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

MAIL_ID = TOKENS["outlook.com mail"]
MAIL_AUTH = TOKENS["outlook.com pass"]
mail_gateway = "hazmatlatif@gmail.com"
smtp = "smtp-mail.outlook.com"
port = 587

def send_mail():  
    with smtplib.SMTP(smtp,port) as server:
        server.starttls()
        server.login(MAIL_ID,MAIL_AUTH)
        msg = MIMEMultipart()
        msg['From'] = MAIL_ID
        msg['To'] = mail_gateway
        msg['Subject'] = f"Happy Birthday!"
        body = content
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        server.sendmail(MAIL_ID,mail_gateway,sms)
    print("Email sent")

import pandas 
birthdays = pandas.read_csv("birthdays.csv")

for index,row in birthdays.iterrows():
    if row["month"] == now_month:
        celebrator = row["name"]
        make_mail()
    else:
        pass






