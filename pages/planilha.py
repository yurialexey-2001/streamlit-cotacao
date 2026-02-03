import streamlit as st
import pandas as pd
import time
from extras import enviar_email_anexo

st.title("Planilha de Controle Financeiro",text_alignment="center")

st.write("""Desenvolvi essa planilha com o objetivo de ajudar no controle de finaças pessoais
         do usuário. Todo mundo já passou pela situação de gastar o dinheiro e não ter idéia de onde ele foi 
         parar. Se você também já passou por isso, essa planilha de gastos vai te ajudar.""")

st.header("Organização da planilha")

st.write("""A planilha tem duas abas, sendo uma para lançamentos diários de entradas e saídas e outra 
         para o acesso ao resumo geral e acompanhamento dos indicadores.""")

st.image("planilha de gastos.png",caption="Aba de acompanhamento (relatório geral)")

st.image("planilha fluxo de caixa.png",caption="Aba de lançamentos de entradas e saídas")

st.write("""Essa planilha foi criada de maneira simples, porém objetiva e fácil de usar, assim, mesmo quem não domina 
            o uso de Excel pode usufruir da planilha.""")

st.header("Quer receber essa planilha para usar no seu dia?")
st.write("""Para receber essa planilha é muito simples, basta preencher o 
         formulário abaixo e eu envio pra você no seu email, ok?😊""")

formulario = st.form(key="enviar planilha")

with formulario:
    nome = st.text_input("Seu nome")
    email = st.text_input("Seu email")
    planilha = pd.read_excel("planilha de controle de gastos.xlsx")

    mensagem = f"""
    <p>Olá {nome}, tudo bem?</p>
    <p>Aqui está a planilha de controle de entradas e saídas prontinha para você.
    <br>Espero que ela possa te ajudar no seu dia-a-dia.</br></p>
    <p>Ah, e ela já está prontinha para uso, basta inserir seus dados, ok?</p>
    <p>Att, Yuri.</p>
    """ 
    enviar_planilha = st.form_submit_button("Receber planilha")

    if enviar_planilha:
        enviar_email_anexo(mensagem=mensagem,destino=email,arquivo=planilha)
        st.success("Email enviado")
        st.info("Redirecionando para Homepage...")
        time.sleep(3)
        st.switch("pages/homepage.py")
