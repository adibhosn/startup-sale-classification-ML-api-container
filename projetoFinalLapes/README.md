# Future-Launch

# Esse projeto foi feito com base em um processo seletivo de um grupo de estudos chamado LAPES 
(disponivel em: https://github.com/lapes-engenharia-de-software/.github/blob/main/profile/ps-lapes-2024.md)

Este projeto utiliza um conjunto de dados sobre startups para prever se uma startup será adquirida ou não. O objetivo principal é analisar os fatores que influenciam o sucesso de uma startup e construir um modelo de Machine Learning que possa prever esse sucesso com base em características específicas.
Para realizar a interface gráfica foi criada uma aplicação web que utiliza Flask como backend (API) e Streamlit como frontend. O projeto permite visualizar insights através de gráficos e realizar previsões personalizadas, tudo orquestrado com Docker.

## Estrutura do Projeto

- **api/**: Arquivos relacionados à API Flask.
- **streamlit/**: Código relacionado ao front-end com Streamlit.
- **docker-compose.yml**: Arquivo para orquestração dos containers Docker.
- **requirements.txt**: Dependências do projeto.
- **Dockerfile**: Arquivo de build da imagem Docker.

## Como Rodar o Projeto

1. Clone o repositório:
   
   git clone https://github.com/Adibhosn/Future-Launch.git

2. Entre no diretório do projeto:
    
    cd PROJETOFINALLAPES

3. Construa e inicie os containers com Docker Compose:
    
    docker-compose up --build

4. Acesse as aplicações:

    http://localhost:8501

Se precisar de mais ajustes ou tiver dúvidas sobre alguma parte específica, estou à disposição!





