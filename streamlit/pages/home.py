import streamlit as st

def home():

    '''Página inicial do aplicativo'''

    # Título da página
    st.markdown("<h1 style='text-align: center; color: green;'>Seja bem vindo ao Future Launch, seu aplicativo de previsão de vendas de startups nos Estados Unidos! 🚀🗽</h1>", unsafe_allow_html=True)

    # Descrição geral do que cada página faz
    st.markdown("""
    ### O que você encontrará em cada página:

    - **Insights**: Visualize gráficos que mostram as maiores chances de venda de startups. Veja o que deu certo em outras startups!
    
    - **Previsão Personalizada**: Faça previsões personalizadas sobre a probabilidade de venda de uma startup, ajustando preferências e parâmetros que refletem suas expectativas.
    
    Explore o dashboard para obter uma visão abrangente do mercado de startups e fazer previsões precisas sobre o sucesso dessas empresas!
    """)
