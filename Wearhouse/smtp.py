import email


import smtplib 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "dezynarh@gmail.com"
pas = "Tylenol123"

sms_gateway = 'hazmatlatif@gmail.com'
# The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
# and port is also provided by the email provider.
smtp = "smtp-mail.outlook.com" 
port = 587
# This will start our email server

with smtplib.SMTP(smtp,port) as server:
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    msg['Subject'] = "First Mail Script\n"
    # Make sure you also add new lines to your body
    body = "Hello World\n"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)

# my_mail = 'dezynarh@gmail.com'
# my_pass = 'Tylenol123'

# with smtplib.SMTP('smtp-mail.outlook.com',587) as connection:
#     connection.ehlo()
#     connection.starttls()

#     # connection = smtplib.SMTP('smtp.mail.yahoo.com',25)
#     # connection.starttls()
#     connection.login(user = my_mail, password = my_pass)
#     connection.sendmail(my_mail,"hazmatlatif@gmail.com",msg='Subject:Remade \n\n!')
#     connection.close()