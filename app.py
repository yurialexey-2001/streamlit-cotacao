import streamlit as st

paginas = st.navigation({
    "Página Inicial":[
        st.Page("pages/homepage.py",title="Home"),
        st.Page("pages/sobre_mim.py",title="Sobre mim")],
    "Conteúdo":[
        st.Page("pages/cotacao.py",title="Cotação de Moedas"),
        st.Page("pages/planilha.py",title="Planilha de Finanças")],
    "Extras":[
        st.Page("pages/feedback.py",title="Página de Feedback")]
        })

paginas.run()