import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
