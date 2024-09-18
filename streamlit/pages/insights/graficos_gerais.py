import streamlit as st
import pandas as pd
from config_front import traduzir_nome

# ---- Funções de exibição de gráficos normais----
def chance_venda(data):
    '''Exibe um gráfico de barras com as categorias com mais chance de venda considerando todas as startups.
    data (dicionário): Um dicionário contendo as taxas de sucesso por categoria.'''

    taxa_sucesso_categoria_data = data['taxa_sucesso_categoria']
    st.subheader('Categorias de Startups com Mais Chance de Venda 💲')
    
    # Traduzindo os nomes das categorias
    taxa_sucesso_categoria = pd.DataFrame(
        [(traduzir_nome(categoria), sucesso) for categoria, sucesso in taxa_sucesso_categoria_data.items()], 
        columns=['Categoria', 'Taxa de Sucesso']
    )
    
    st.bar_chart(taxa_sucesso_categoria.set_index('Categoria'))

def estado_venda(data):
    '''Exibe um gráfico de barras com os estados com mais startups vendidas considerando todas as startups.
    data(dicionário): Um dicionário contendo as taxas de sucesso por estado.'''

    taxa_sucesso_estado_data = data['taxa_sucesso_estado']
    st.subheader('Estados com Mais Startups Vendidas 📍')
    
    # Traduzindo os nomes dos estados
    taxa_sucesso_estado = pd.DataFrame(
        [(traduzir_nome(estado), sucesso) for estado, sucesso in taxa_sucesso_estado_data.items()], 
        columns=['Estado', 'Taxa de Sucesso']
    )
    
    st.bar_chart(taxa_sucesso_estado.set_index('Estado'))
