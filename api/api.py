from flask import Flask, request, jsonify
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from config_api import ESTADOS, CATEGORIAS


app = Flask(__name__)

# Carregando os dados
data = pd.read_csv('df_tratado_startups.csv')

# Aplicando o SMOTE nos dados
X = data.drop('status', axis=1)
y = data['status']

# Instanciando o SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.25, random_state=40)

# Pipeline de treinamento
pipeline = Pipeline([
    ('selecao_de_features', SelectKBest(f_classif, k=2)),
    ('classificador', GaussianNB())
])

# Treinando o modelo
pipeline.fit(X_train, y_train)

# Rota para prever o status de uma startup
@app.route('/previsao_personalizada', methods=['POST'])
def prever():
    dados_usuario = request.get_json()

    # Criando o dicionário com as colunas de input zeradas
    dados_entrada = {col: 0 for col in X.columns}

    # Atualizando estado e categoria com as escolhas do usuário
    dados_entrada[f'is_{dados_usuario["estado"]}'] = 1
    dados_entrada[f'is_{dados_usuario["categoria"].lower()}'] = 1

    # Atualizando com os outros valores fornecidos pelo usuário
    dados_entrada.update({
        'relationships': dados_usuario['relationships'],
        'funding_rounds': dados_usuario['funding_rounds'],
        'funding_total_usd': dados_usuario['funding_total_usd'],
        'milestones': dados_usuario['milestones'],
        'has_VC': dados_usuario['has_VC'],
        'has_angel': dados_usuario['has_angel'],
        'has_roundA': dados_usuario['has_roundA'],
        'has_roundB': dados_usuario['has_roundB'],
        'has_roundC': dados_usuario['has_roundC'],
        'has_roundD': dados_usuario['has_roundD'],
        'avg_participants': dados_usuario['avg_participants'],
        'is_top500': dados_usuario['is_top500']
    })

    # Convertendo o dicionário em DataFrame
    entrada_usuario = pd.DataFrame([dados_entrada])

    # Fazendo a previsão
    previsao = pipeline.predict(entrada_usuario)

    return jsonify({"previsao": int(previsao[0])})

# Rota para obter insights sobre a taxa de sucesso
@app.route('/taxa-sucesso', methods=['GET'])
def taxa_sucesso():

    # Calculando a taxa de sucesso por categoria
    taxa_sucesso_categoria = {}
    for col in CATEGORIAS:
        sucesso = data[data['status'] == 1][col].sum()
        total = data[col].sum()
        if total > 0:
            taxa_sucesso_categoria[col] = sucesso / total

    # Calculando a taxa de sucesso por estado
    taxa_sucesso_estado = {}
    for col in ESTADOS:
        sucesso = data[data['status'] == 1][col].sum()
        total = data[col].sum()
        if total > 0:
            taxa_sucesso_estado[col] = sucesso / total

    return jsonify({
        'taxa_sucesso_categoria': taxa_sucesso_categoria,
        'taxa_sucesso_estado': taxa_sucesso_estado,
    })


@app.route('/media_por_feature', methods=['GET'])
def media_features():
    # Filtra as colunas binárias (número único de valores igual a 2) e não-binárias (mais de 2 valores distintos)
    colunas_binarias = [col for col in data.columns if data[col].nunique() == 2]
    colunas_naobinarias = [col for col in data.columns if data[col].nunique() > 2]

    # Filtro de startups vendidas (status == 1)
    startups_vendidas = data[data['status'] == 1]

    # Cálculo das médias das colunas não-binárias
    media_features_nao_binarias = startups_vendidas[colunas_naobinarias].mean().round(2).to_dict()

    # Cálculo da quantidade de 0s e 1s para as colunas binárias
    distrib_features_binarias = {}
    for col in colunas_binarias:
        zeros = (startups_vendidas[col] == 0).sum()
        uns = (startups_vendidas[col] == 1).sum()
        
        # Adiciona ao dicionário apenas se houver 0s ou 1s
        distrib_features_binarias[col] = {
            '0s': int(zeros),  # Convertendo para int
            '1s': int(uns)    # Convertendo para int
        }

    # Retorna os dados como resposta JSON   
    return jsonify({
        'media_features_nao_binarias': {k: float(v) for k, v in media_features_nao_binarias.items()},  # Convertendo para float
        'distrib_features_binarias': distrib_features_binarias
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
