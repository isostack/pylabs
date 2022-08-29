import requests

# ======== Get item page ========
URL = "https://www.amazon.com/ASUS-Gaming-VG27AQ-G-SYNC-Monitor/dp/B07WQ4FXY9/ref=sr_1_10?keywords=asus%2Btuf&qid=1661700909&sr=8-10&th=1"
head_neta = {
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=head_neta)

# ======== Scrap item web data ============
import bs4

soup = bs4.BeautifulSoup(response.text, "lxml")

item_price = soup.find("span", class_="a-offscreen").text

price = float(item_price.replace("$", ""))

# ======== Check and send price notification mail ====
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

alert_state = False

if price < 280:
    alert_state = True

    email_gateway = "dezynarh@gmail.com"
    smtp = "smtp-mail.outlook.com"
    port = 587
    USERNAME = "dezynarh@gmail.com"
    AUTH="Tylenol123"
    
    with smtplib.SMTP(smtp,port) as server:
        server.starttls()
        server.login(USERNAME,AUTH)
        msg = MIMEMultipart()
        msg['From'] = "Insomnia.corp"
        msg['To'] = email_gateway
        msg['Subject'] = f"Low price alert !!!!"
        body = f"The price of your item has lowered to {item_price}"
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        server.sendmail(USERNAME,email_gateway,sms)
    print("Email sent")
    
 