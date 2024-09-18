import streamlit as st
from pages.previsao_personalizada.previsao_personalizada import previsao_personalizada
from pages.insights.insights import insights
from pages.home import home

# Inicializar o estado da sessão para 'role' se ainda não existir (caso haja controle de autenticação futura)
if "role" not in st.session_state:
    st.session_state.role = "User" 

# Definir o título da página e a logo
st.set_page_config(page_title="FutureLaunch", page_icon=":rocket:")

# Definir as páginas que o usuário pode acessar

home_page = st.Page(
    home, 
    title="Home", 
    icon="🏠", 
    default=True
)

previsao_page= st.Page(
    previsao_personalizada, 
    title="Previsão Personalizada", 
    icon="🔮"
)

insights_page = st.Page(
    insights, 
    title="Insights", 
    icon="📊"
)

# Definir um grupo de páginas acessíveis
page_dict = {"Menu": [home_page, previsao_page, insights_page]}

# Bloco principal
def main():
    # Criar a navegação dinâmica
    pg = st.navigation(page_dict)
    
    # Executar a página selecionada
    pg.run()

if __name__ == "__main__":
    main()
