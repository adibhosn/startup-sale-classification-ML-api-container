import streamlit as st
import requests
from pages.insights.graficos_gerais import venda_categoria, venda_estado
from pages.insights.graficos_interativos import exibir_media_feature_nao_binaria, exibir_grafico_pizza_feature_binaria

def insights():

    '''Função para fazer as requisições da api, e chamar as funções de exibição dos gráficos.'''

    st.markdown("<h1 style='text-align: center; color: #A52DE1;'>Insights sobre Startups 📊</h1>", unsafe_allow_html=True)


    # Requisição para obter a taxa de sucesso por categoria e estado
    requisicao = requests.get('http://flask_api:5003/soma_vendas')
    if requisicao.status_code == 200:
        data = requisicao.json()
        venda_categoria(data)
        venda_estado(data)
    else:
        st.write('Erro ao obter dados da API.')

    st.subheader('Verificação de variáveis específicas✅ ')
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Chama a API para obter os dados
    resposta = requests.get('http://flask_api:5003/media_por_feature')

    if resposta.status_code == 200:
        data1 = resposta.json()
        st.markdown("**Média de atributos em startups vendidas**👇")
        exibir_media_feature_nao_binaria(data1)

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown("**Distribuição de atributos para verificação de quais representam maior percentual de venda** 👇")
        exibir_grafico_pizza_feature_binaria(data1)
    else:
        st.write('Erro ao obter dados da API.')
