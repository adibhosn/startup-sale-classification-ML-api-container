# Definindo listas de estados e categorias para previsão
ESTADOS = ['MA', 'TX', 'CA', 'NY', 'otherstate']
CATEGORIAS = ['software', 'web', 'mobile', 'enterprise', 'advertising',
              'gamesvideo', 'ecommerce', 'biotech', 'consulting', 'othercategory']


# Dicionário de mapeamento das variáveis
nome_variaveis = {
    'relationships': 'Relacionamentos',
    'funding_rounds': 'Rodadas de Financiamento',
    'funding_total_usd': 'Total de Financiamento (USD)',
    'milestones': 'Marcos Atingidos',
    'is_CA': 'Está na Califórnia',
    'is_NY': 'Está em Nova York',
    'is_MA': 'Está em Massachusetts',
    'is_TX': 'Está no Texas',
    'is_otherstate': 'É de Outro Estado',
    'is_software': 'É de Software',
    'is_web': 'É de Web',
    'is_mobile': 'É de Aplicativos Mobile',
    'is_enterprise': 'É de Enterprise',
    'is_advertising': 'É de Publicidade',
    'is_gamesvideo': 'É de Jogos/Vídeo',
    'is_ecommerce': 'É de Comércio Eletrônico',
    'is_biotech': 'É de Biotecnologia',
    'is_consulting': 'É de Consultoria',
    'is_othercategory': 'É Outra Categoria',
    'has_VC': 'Tem Capital de Risco',
    'has_angel': 'Tem Investidor Anjo',
    'has_roundA': 'Tem Rodada A',
    'has_roundB': 'Tem Rodada B',
    'has_roundC': 'Tem Rodada C',
    'has_roundD': 'Tem Rodada D',
    'avg_participants': 'Média de Participantes',
    'is_top500': 'Esta no Top 500',
    'status': 'Status'
}

# Função para traduzir nomes das variáveis
def traduzir_nome(nome):
    return nome_variaveis.get(nome, nome)