import streamlit as st
from config_front import traduzir_nome
import matplotlib.pyplot as plt

# Função para exibir a média de uma feature não binária
def exibir_media_feature_nao_binaria(data1):

    '''Exibe a média de features não binárias para *startups vendidas*.
    data1 (dicionário): Um dicionário contendo as médias das features não binárias e a distribuição das features binárias.'''

    media_features_nao_binarias = data1['media_features_nao_binarias']

    # Interface para o usuário escolher uma feature não binária
    opcoes = {traduzir_nome(chave): chave for chave in media_features_nao_binarias.keys()}
    feature_naobinaria = st.selectbox("Escolha uma feature não binária", list(opcoes.keys()))

    # Exibe a média da feature selecionada para startups vendidas
    chave_original = opcoes[feature_naobinaria]
    media = media_features_nao_binarias.get(chave_original, None)
    if media is not None:
        st.write(f"Média de {feature_naobinaria} para startups vendidas: {media}")
    else:
        st.write(f"Não há dados suficientes para {feature_naobinaria}.")

# Função para exibir os gráficos interativos (pizza) para features binárias
def exibir_grafico_pizza_feature_binaria(data1):

    '''Exibe um gráfico de pizza para uma feature binária para *startups vendidas* em um gráfico interativo no Streamlit.
    data1 (dicionário): Um dicionário contendo as médias das features não binárias e a distribuição das features binárias.'''

    distrib_features_binarias = data1['distrib_features_binarias']

    # Interface para o usuário escolher uma feature binária
    opcoes = {traduzir_nome(chave): chave for chave in distrib_features_binarias.keys()}
    feature_binaria = st.selectbox("Escolha uma feature binária", list(opcoes.keys()))

    # Obtém o valor da distribuição para startups vendidas
    chave_original = opcoes[feature_binaria]
    valor = distrib_features_binarias.get(chave_original, None)
    if valor is not None:
        zeros = valor.get('0s', 0)
        uns = valor.get('1s', 0)

        # Plotando gráfico de pizza
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#0E1117')
        ax.pie([zeros, uns], labels=['Fechadas', 'Vendidas'], autopct='%1.1f%%', colors=['#C20700', '#11C21D'], textprops={'color':"white"})
        st.pyplot(fig)
    else:
        st.write(f"Não há dados suficientes para {feature_binaria}.")