import urllib.request
import time
import os
from email.message import EmailMessage
import smtplib
import ssl   
    
    
email_sender = "comprarbeans@gmail.com"
email_password = "jsxerzzufmbwmkve"
email_receiver = "camilagomesbsi@gmail.com"

subject = "Compre Beans"
body = "Teste"

em = EmailMessage()

em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())