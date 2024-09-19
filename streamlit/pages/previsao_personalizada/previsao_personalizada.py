import streamlit as st
from pages.previsao_personalizada.enviar_coletar_dados_previsao import coletar_dados, enviar_previsao

def exibir_texto():
    '''Exibe o texto de introdução da página.'''

    st.markdown(
        "<h1 style='text-align: center; color: #00A0E0;'>Previsão Personalizada de Venda de Startups 🔮</h1>",unsafe_allow_html=True)
    st.markdown('''
    ### Bem-vindo à ferramenta de previsão de venda de startups! 🚀
    Insira as informações abaixo para prever se sua startup tem grandes chances de ser vendida ou não.
    ''')

def exibir_resultado(predicao):
    '''Exibe o resultado da previsão para o usuário de forma visual'''

    if predicao is None:
        st.markdown("<h3 style='color: orange;'>Não foi possível obter uma previsão. Tente novamente mais tarde.</h3>", unsafe_allow_html=True)
    elif predicao == 1:
        st.markdown("<h3 style='color: green;'>A startup tem grandes chances de ser vendida! 💰</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: red;'>A startup provavelmente não será vendida. 😔</h3>", unsafe_allow_html=True)

def previsao_personalizada():
    '''Função principal da página de Previsão Personalizada, chama a requisição, exibe o texto
      define os dados com base na função coletar_dados(), depois envia-os com base na função enviar_previsao(dados, requisição)
      além de exibir o resultado para o usuário.'''
    
    #definindo url da requisição
    requisicao = 'http://flask_api:5003/previsao_personalizada'

    exibir_texto()
    
    dados = coletar_dados()

    if st.button('Prever'):
        predicao = enviar_previsao(dados, requisicao)
        exibir_resultado(predicao)
