import streamlit as st
import time

st.title("Seja bem vindo ao meu projeto!",text_alignment="center")

col1,col2,col3 = st.columns([1,2,1])
with col2:
    st.image("Logo-Hashtag-Original-1024x458.png",width=278)

st.write("""Esse app foi desenvolvido para a participação no 1° desafio da comunidade impressionadora da 
         Hashtag Treinamentos. Talvez esse app possa não ser algo que contribui diretamente para a vida dos
         membros da comunidade, mas como outros fatores também estão sendo avaliados, acho que vale a tentativa.""")

st.title("O que você encontrará aqui?")

st.write("#### Cotação de moedas com gráfico de variação 📊")

st.write("""Nessa aba, você consegue consultar os valores de algumas moedas e fazer a 
             conversão para Real (R$). Além disso, é possível fazer uma análise de variação
             ao longo do tempo, basta inserir a quantidade de dias que deseja analisar.""")

st.image("image.png",caption="O gráfico retornado é semelhante a esse.")

coluna1,coluna2,coluna3 = st.columns([1,1,1])

with coluna2:
    if st.button("Cotação de Moedas"):
        st.switch_page("pages/cotacao.py")
    




        


