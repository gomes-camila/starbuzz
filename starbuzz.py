import urllib.request
import time
import os
from email.message import EmailMessage
import smtplib
import ssl


def main():
    while True:
        print("Procura preço")

        verifica_compra(pesquisa_preco())

        time.sleep(10)

def escolhe_url():
    urls = [
        "http://beans.itcarlow.ie/prices-loyalty.html",
        "http://beans.itcarlow.ie/prices.html"
    ]
    

def pesquisa_preco():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto  = pagina.read().decode("utf8")

    inicio = texto.find(">$") + 2
    fim  = inicio + 4
    preco = texto[inicio:fim]
    
    preco = float(preco)
    print(preco)
    return preco
    

def verifica_compra(par_preco):
    while True:
        if par_preco < 4.70:
            print(f"Comprar! Preço: {par_preco}")
            mandar_email(par_preco)
        else:
            print(f"Espere! Preço: {par_preco}")
        time.sleep(10)


def mandar_email(par_preco):
    email_sender = "comprarbeans@gmail.com"
    email_password = "jsxerzzufmbwmkve"
    email_receiver = "camilagomesbsi@gmail.com"

    subject = "Compre Beans"
    body = f"Compre Beans, Preço: {par_preco}"
    em = EmailMessage()

    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        

main()