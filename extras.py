import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import streamlit as st

def enviar_email(mensagem,destino):

    msg = MIMEMultipart()

    msg["Subject"] = "Olá, gratidão pelo feedback!"
    msg["From"] = "yuritreinos@gmail.com"
    msg["To"] = destino

    msg.attach(MIMEText(mensagem,"html"))

    servidor = smtplib.SMTP("smtp.gmail.com",587)
    servidor.starttls()
    servidor.login(user=msg["From"],password=st.secrets["MINHA_SENHA"])
    servidor.send_message(msg)
    servidor.quit()

def enviar_email_anexo(destino,mensagem,arquivo):
    msg = MIMEMultipart()

    msg["Subject"] = "Sua planilha chegou!"
    msg["From"] = "yuritreinos@gmail.com"
    msg["To"] = destino

    msg.attach(MIMEText(mensagem,"html"))

    with open("planilha de controle de gastos.xlsx","rb") as arquivo:
        msg.attach(MIMEApplication(arquivo.read(),Name="Planilha controle de entradas e saídas.xlsx",_subtype="xlsx")) 

    servidor = smtplib.SMTP("smtp.gmail.com",587)
    servidor.starttls()
    servidor.login(user=msg["From"],password=st.secrets["MINHA_SENHA"])
    servidor.send_message(msg)
    servidor.quit()
