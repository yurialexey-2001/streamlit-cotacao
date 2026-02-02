from google.oauth2.service_account import Credentials
import streamlit as st
import gspread

def adicionar_feedback(nome_usuario, email_usuario, estrelas_usuario, msg_usuario):
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )

    client = gspread.authorize(creds)
    planilha = client.open_by_key(
    "1IUvgtb4uyraC1ffe-JWEY-14l3t1UkCnIq7Cbbt6tsw").sheet1


    planilha.append_row([
        nome_usuario,
        email_usuario,
        estrelas_usuario,
        msg_usuario
    ])


