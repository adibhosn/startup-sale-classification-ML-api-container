import streamlit as st
import requests
from config_front import ESTADOS_previsao, CATEGORIAS_previsao

def coletar_dados():

    '''Coleta os dados inseridos pelo usuário no Streamlit e retorna um dicionário com esses dados.'''

    # Coleta as escolhas do usuário feitas no Streamlit.
    st.markdown('#### Escolha o Estado e a Categoria da Startup:')
    estado = st.selectbox('Estado', ESTADOS_previsao)
    categoria = st.selectbox('Categoria', CATEGORIAS_previsao)

    st.markdown('#### Insira os Valores das Outras Features:')
    relationships = st.number_input('Relações', min_value=0)
    funding_rounds = st.number_input('Rodadas de Financiamento', min_value=0)
    funding_total_usd = st.number_input('Total de Financiamento em USD', min_value=0.0)
    milestones = st.number_input('Marcos Alcançados', min_value=0)
    avg_participants = st.number_input('Média de Participantes', min_value=0)
    
    # Para variáveis booleanas, exibir "Sim" e "Não" e armazenar como 1 e 0
    has_VC = st.radio('Tem Capital de Risco?', ['Sim', 'Não'])
    has_angel = st.radio('Tem Investidor Anjo?', ['Sim', 'Não'])
    has_roundA = st.radio('Rodada A?', ['Sim', 'Não'])
    has_roundB = st.radio('Rodada B?', ['Sim', 'Não'])
    has_roundC = st.radio('Rodada C?', ['Sim', 'Não'])
    has_roundD = st.radio('Rodada D?', ['Sim', 'Não'])
    
    is_top500 = st.radio('Está no Top 500?', ['Sim', 'Não'])

    # Converter as escolhas "Sim" e "Não" para 1 e 0
    return {
        'estado': estado,
        'categoria': categoria,
        'relationships': relationships,
        'funding_rounds': funding_rounds,
        'funding_total_usd': funding_total_usd,
        'milestones': milestones,
        'avg_participants': avg_participants,
        'has_VC': 1 if has_VC == 'Sim' else 0,
        'has_angel': 1 if has_angel == 'Sim' else 0,
        'has_roundA': 1 if has_roundA == 'Sim' else 0,
        'has_roundB': 1 if has_roundB == 'Sim' else 0,
        'has_roundC': 1 if has_roundC == 'Sim' else 0,
        'has_roundD': 1 if has_roundD == 'Sim' else 0,
        'is_top500': 1 if is_top500 == 'Sim' else 0
    }

def enviar_previsao(dados, requisicao):

    '''Envia os dados inseridos pelo usuário para a API e retorna a previsão feita pela API.'''
    
    try:
        response = requests.post(requisicao, json=dados)
        response.raise_for_status()  # Gera uma exceção se a resposta contiver um erro HTTP
        return response.json()['previsao']
    except requests.exceptions.RequestException as e:
        st.error(f'Ocorreu um erro ao enviar a solicitação: {e}')
        return None