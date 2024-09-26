import streamlit as st
import pandas as pd
from config_front import traduzir_nome

# ---- Funções de exibição de gráficos normais----
def venda_categoria(data):
    '''Exibe um gráfico de barras com as categorias com mais vendas considerando apenas as quantidades de startups.
    (sem levar em conta percentual).
    data (dicionário): Um dicionário contendo as somas de vendas por categoria.'''

    soma_vendas_categoria_data = data['soma_vendas_categoria']
    st.subheader('Número de vendas por categoria de startup 💲')
    
    # Traduzindo os nomes das categorias
    soma_vendas = pd.DataFrame(
        [(traduzir_nome(categoria), vendas) for categoria, vendas in soma_vendas_categoria_data.items()], 
        columns=['Categoria', 'soma de vendas']
    )
    
    st.bar_chart(soma_vendas.set_index('Categoria'))

def venda_estado(data):
    '''Exibe um gráfico de barras com os estados com mais vendas considerando apenas as quantidades de startups 
    (sem levar em conta percentual).
    data(dicionário): Um dicionário contendo as somas de vendas por estado.'''

    soma_vendas_estado_data = data['soma_vendas_estado']
    st.subheader('Número de vendas por estados em que localizam as startups 📍')
    
    # Traduzindo os nomes dos estados
    soma_vendas_estado = pd.DataFrame(
        [(traduzir_nome(estado), vendas) for estado, vendas in soma_vendas_estado_data.items()], 
        columns=['Estado', 'soma de vendas']
    )
    
    st.bar_chart(soma_vendas_estado.set_index('Estado'))
