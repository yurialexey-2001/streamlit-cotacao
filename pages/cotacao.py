import streamlit as st
import yfinance
import plotly.express as px
import pandas as pd
from extras import enviar_email

moedas = {"Dólar Americano": "USDBRL=X",
            "Euro": "EURBRL=X",
            "Libra Esterlina": "GBPBRL=X",
            "Iene Japonês": "JPYBRL=X",
            "Franco Suíço": "CHFBRL=X",
            "Dólar Canadense": "CADBRL=X",
            "Dólar Australiano": "AUDBRL=X",
            "Yuan Chinês": "CNYBRL=X",
            "Peso Argentino": "ARSBRL=X",
            "Peso Mexicano": "MXNBRL=X",
            "Peso Chileno": "CLPBRL=X",
            "Rand Sul-Africano": "ZARBRL=X"}

st.title("Cotação de Moedas",text_alignment="center")

st.write("""Aqui você consegue acompanhar a variação do preço das moedas selecionadas ao longo do tempoo selecionado.
         Você pode selecionar várias moedas, porém como essa aplicação consome dados de uma API, ao selecionar todos as 
         opções muito rápido, pode dar erro. Para que tudo funcione normalmente, clique em cada moeda, aguarde um segundo 
         e selecione a(s) outra(s).""")

col1,col2 = st.columns([2,1])
with col1:
    moeda = st.multiselect(label="Moedas",options=moedas.keys())
with col2:
    periodo = st.selectbox(label="Periodo",options=["1d","1mo","3mo","6mo","1y","5y"])

dfs = []

if moeda and periodo:
    if periodo != "1d":
        for coin in moeda:
            codigo = moedas[coin]

            cotacao = yfinance.download(codigo,period=periodo)[["Close"]]

            cotacao = pd.DataFrame(cotacao).reset_index()
            cotacao.columns = cotacao.columns.droplevel(1)
            
            cotacao["Moeda"] = coin
            
            dfs.append(cotacao)

        df_final = pd.concat(dfs)

        fig = px.line(df_final,x="Date",y="Close",color="Moeda",template="ggplot2")
        fig.update_xaxes(showgrid=True,title_text="Data")
        fig.update_yaxes(title_text="Valor em Reais (R$)")
        st.plotly_chart(fig)

    else:
        for coin in moeda:
            codigo = moedas[coin]
            cotacao = yfinance.download(codigo,period=periodo)[["Close"]]

            cotacao = pd.DataFrame(cotacao).reset_index()
            cotacao.columns = cotacao.columns.droplevel(1)

            valor_moeda = cotacao["Close"].iloc[-1]
            valor_moeda = str(valor_moeda)
            valor_moeda = valor_moeda[:4]


            st.metric(label=f"Valor de {coin} hoje",value=f"R$ {valor_moeda}")