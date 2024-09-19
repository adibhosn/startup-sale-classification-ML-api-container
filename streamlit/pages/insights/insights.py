import streamlit as st
import requests
from pages.insights.graficos_gerais import chance_venda, estado_venda
from pages.insights.graficos_interativos import exibir_media_feature_nao_binaria, exibir_grafico_pizza_feature_binaria

def insights():

    '''Função para fazer as requisições da api, e chamar as funções de exibição dos gráficos.'''

    st.markdown("<h1 style='text-align: center; color: #A52DE1;'>Insights sobre Startups 📊</h1>", unsafe_allow_html=True)

    st.markdown("_Levando em conta todas as startups_")

    # Requisição para obter a taxa de sucesso por categoria e estado
    requisicao = requests.get('http://flask_api:5003/taxa-sucesso')
    if requisicao.status_code == 200:
        data = requisicao.json()
        chance_venda(data)
        estado_venda(data)
    else:
        st.write('Erro ao obter dados da API.')

    st.subheader('Verificação de variáveis levando em conta apenas startups que foram vendidas ✅')

    # Chama a API para obter os dados
    resposta = requests.get('http://flask_api:5003/media_por_feature')

    if resposta.status_code == 200:
        data1 = resposta.json()
        exibir_media_feature_nao_binaria(data1)
        exibir_grafico_pizza_feature_binaria(data1)
    else:
        st.write('Erro ao obter dados da API.')
