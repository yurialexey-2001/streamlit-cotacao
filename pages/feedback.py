import streamlit as st
from extras import enviar_email
from bancodedados import adicionar_feedback
import time

formulario = st.form(key="feedback")

with formulario:

    st.title("Página de Feedback",text_alignment="center")
    nome = st.text_input("Seu nome")
    email = st.text_input("Seu email")
    qtd_estrelas = ["1","2","2","4","5"]
    util = ["Sim","Não"]
    
    st.write("#### Avalie a funcionalidade da cotação de moedas:")

    col1,col2,col3 = st.columns([1,1,1])
    with col2:
        feedback_cotacao = st.feedback(options="stars")

    st.write("#### A planilha de controle financeiro vai ser útil pra você?")
    colA,colB,colC = st.columns([1,1,1])
    with colB:
        feedback_planilha = st.feedback(options="thumbs")
    
    melhoria = st.text_input(label="feedback",label_visibility="hidden",
                  placeholder="Escreva aqui um comentário sobre a aplicação e/ou indique melhorias")
    
    if st.form_submit_button("Enviar feedback"):
        if feedback_planilha is None or feedback_cotacao is None or not email or not nome:
            st.warning("Preencha tudo antes de enviar")
        else:
            adicionar_feedback(nome_usuario=nome,email_usuario=email,
                               estrelas_usuario=qtd_estrelas[feedback_cotacao],
                               msg_usuario=melhoria,utilidade=util[feedback_planilha])
            
            if feedback_cotacao < 3:
                msg_negativa = f"""
                <p>Olá, {nome} tudo bem?</p>
                
                <p>Venho por meio desse email agradecer sua avaliação de <strong>{qtd_estrelas[feedback_cotacao]} estrela(s)</strong>
                no meu projeto.<br>É uma pena que sua experiência aqui não tenha sido a melhor, mas com o seu feedback prometo
                que irei melhorar ainda mais.</p>
                <p>Ah, e eu também tô vendo sua mensagem de melhoria aqui viu! Obrigado por contribuir.</p>
                <p>Abraços, Yuri.</p>
                """
                enviar_email(destino=email,mensagem=msg_negativa)

            else:
                msg_positiva = f"""
                <p>Olá, {nome} tudo bem?</p>
                
                <p>Venho por meio desse email agradecer sua avaliação de <strong>{qtd_estrelas[feedback_cotacao]} estrela(s)</strong>
                no meu projeto.<br>É muito gratificante pra mim saber que está tudo certo por aqui.</p>
                <p>Ah, e eu também tô vendo sua mensagem de melhoria aqui viu! Obrigado por contribuir.</p>"""
                enviar_email(destino=email,mensagem=msg_positiva)

            st.success("Feedback coletado!")
            st.info("Redirecionando você para a homepage...")
            time.sleep(3)
            st.switch_page("pages/homepage.py")
            
        


