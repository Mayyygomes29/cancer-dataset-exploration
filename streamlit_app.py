import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.visualization.graphs import plot_bar, plot_correlation,plot_disper
from main import main


resultados = main()

#================================
#USANDO OS GRÁFICOS NO STREAMLIT
#================================
def analise_corr(valor, titulo):
        analise = resultados[valor]
        plot = plot_correlation(analise, titulo)
        return st.pyplot(plot)

def analise_bar(valor, titulo, cor):
        analise = resultados[valor]
        plot = plot_bar(analise, titulo, cor)
        return st.pyplot(plot)

def analise_table(titulo, valor ):
        st.write(f'###### **{titulo}**')
        analise = resultados[valor]
        return st.table(analise,border=True, height='stretch')
      
def analise_dispersao(valor, x, y, hue, titulo):
        analise = resultados[valor]
        plot = plot_disper(analise, x, y, hue, titulo)
        st.pyplot(plot) 


#=====================
#PÁGINAS DO STREAMLIT
#=====================
def page_home():
    st.title(":red[DataFrame] - Análise de Câncer", text_alignment='center')
    st.write(resultados['df'].head(50).round(2))


def page_eda():
    st.title(":red[EDA] - Análise de Câncer", text_alignment='center')
    st.metric(label="Total de Pacientes", value=len(resultados['df']))

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        analise_corr('correlacao_variaveis', 'Correlação entre variáveis' )
    with col2:
        analise_bar('classificacao_mcp', 'Analisando MCP1', 'green')
    with col3:
        analise_bar('classificacao_insulina', 'Analisando Insulina', 'green')
    with col4:
        analise_bar('classificacao_glicose','Analisando Glicose', 'green')


def page_model():
    st.title(":red[MODELO] - Análise de Câncer", text_alignment='center')
    st.markdown("LEGENDA: :blue-background[0 - Sem Câncer]  :red-background[1 - Com Câncer] ", text_alignment='center')
    col5, col6= st.columns(2)
    col7, col8  = st.columns(2)
    col9, col10  = st.columns(2)
    col11, col12= st.columns(2)
    col13, col14 = st.columns(2)

    with col5:
        analise_bar('qnt_cancer', 'Quantidade x Câncer', 'blue')
    with col6:
        analise_bar('qnt_cluster', 'Quantidade por Cluster','blue')
    with col7:
         analise_corr('contigencia', 'Proporção de cluster com câncer')
    with col8:
        analise_corr('media_variaveis_cancer', 'Média de variavéis por câncer')    
    with col11:
        st.markdown("Níveis de MCP-1: **:green-background[0- Normal] :yellow-background[1- Moderado] :red-background[2- Alto]** ")
        analise_table('Proporção de MCP-1 C/ Câncer e S/ Câncer','mcp_cancer')
    with col12:
        analise_bar('media_idade_cancer', 'Média Idade C/ Câncer e S/ Câncer', 'blue')
    with col9:
        analise_dispersao('df','Insulina','Idade','cluster', 'Dispersão da Idade por cluster')
    with col10:
        analise_corr('medias_variaveis_cluster', 'Média de variáveis por cluster') 
    with col13:
        analise = resultados['classificacao']
        analise = analise['df_result']
        analise = analise[['real', 'previsto', 'probabilidade']]
        fig = plot_disper(analise, 'real', 'probabilidade', 'previsto', 'Dispersão da Probabilidade de Câncer')
        st.pyplot(fig)


def page_metrics():
    st.title(":red[Métricas] - Modelo de Classificação", text_alignment='center')
    col1 , col2 = st.columns(2)
    with col1:
         analise = resultados['classificacao']
         analise = analise['metrics']
         st.table(analise)


st.markdown("""
<style>

/* Fundo da sidebar */
section[data-testid="stSidebar"] {
    background-color: #001f3f !important;
}

/* Área do navigation */
[data-testid="stSidebarNav"] {
    background-color: #001f3f !important;
}

/* Texto geral */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Itens do menu */
[data-testid="stSidebarNav"] a {
    color: white !important;
    border-radius: 8px;
    padding: 6px;
}

/* Item selecionado */
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #003366 !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


pg = st.navigation([
    st.Page(page_home, title='Home'),
    st.Page(page_eda, title="Análise Exploratória"),
    st.Page(page_model, title="Análise de Modelo"),
    st.Page(page_metrics, title='Métricas do Modelo')
])

pg.run()