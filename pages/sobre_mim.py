import streamlit as st

st.title("Quem sou eu?",text_alignment="center")

st.write("""#### Oi, eu sou o Yuri!""")


st.write("""Tenho 24 anos e recentemente me graduei em Administração. Moro no interior de Minas Gerais e busco sempre
         aprender para que meu horizonte de possibilidades possa ser expandido.""")


col1,col2 = st.columns([1,1])

with col1:
    st.write("##### Você pode me contatar ou se conectar comigo por aqui")
    #card do email
    with st.container(border=True):
        colA,colB = st.columns([1,2])
        with colA:
            st.image("gmail_logo.png",width=27)
        with colB:
            st.write("yuriadm2025@gmail.com")
    #card do linkedin
    with st.container(border=True):
        colC,colD = st.columns([1,2])
        with colC:
            st.image("logo_linkedin.png",width=27)
        with colD:
            st.page_link(page="https://www.linkedin.com/in/yuri-oliveira-6a1bb1240/",label="Yuri Oliveira")
    #card do github
    with st.container(border=True):
        colE,colF = st.columns([1,2])
        with colE:
            st.image("github.png",width=27)
        with colF:
            st.page_link(page="https://github.com/yurialexey-2001",label="GitHub")

with col2:
    st.image("eu_formando.jpeg",width=200,caption="Esse sou eu no dia da formatura")


st.write("""
         Podem haver erros/bugs aqui, e eu estou aberto a feedbacks. Para isso, deixei um botão abaixo que te direcionará 
         para uma página onde você poderá me dizer em que posso melhorar esse projeto.
         Obrigado!""")

if st.button("Clique aqui para dar um feedback"):
    st.switch_page("pages/feedback.py")
