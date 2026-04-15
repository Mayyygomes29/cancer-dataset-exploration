import pandas as pd

FEATURES = [
    'Idade', 'IMC', 'Glicose', 'Insulina',
    'HOMA', 'Leptina', 'Adiponectina',
    'Resistina', 'MCP1'
]


# =============================
# ANALISAR CLASSIFICAÇÃO MCP-1/INSULINA/GLICOSE
# =============================
def analyse_classification(df, nome):
    return df[nome].value_counts()


# =============================
# CORRELAÇÃO ENTRE VARIÁVEIS
# =============================
def variable_correlation(df):
    variaveis_correlacao = df[FEATURES].corr()
    return variaveis_correlacao


#-------------------------------------------------------------------------------------------------
# EXPLORANDO MODELOS
#-------------------------------------------------------------------------------------------------

#==============================================
# TABELA DE CONTIGÊNCIA ENTRE CLUSTER E CÂNCER
#==============================================
def analyse_contig(df):
    analise = pd.crosstab(df['cluster'], df['cancer'], normalize='index') * 100
    analise = analise.round(2)
    return analise

#=========================
# MÉDIA IDADE COM CÂNCER
#=========================
def analyse_age_cancer(df):
    idade_cancer = df.groupby('cancer')['Idade'].mean().astype(int)
    return idade_cancer


#=========================
# PESSOAS COM CÂNCER
#=========================
def analyse_qnt_cancer(df):
    return df['cancer'].value_counts()


#================================
# QUANTIDADE DE PESSOA POR CLUSTER
#================================
def analyse_cluster(df):
    return df['cluster'].value_counts()


#================================
# MÉDIA DAS VARIÁVEIS POR CLUSTER
#================================
def analyse_mean_variable_cluster(df):
    return df.groupby('cluster')[FEATURES].mean().round(2)


#==========================================
# MÉDIA DAS VARIÁVEIS COM CÂNCER E S/ CÂNCER
#==========================================
def analyse_mean_variable_cancer(df):
    return df.groupby('cancer')[FEATURES].mean().round(2).T



#=====================================
#PROPOÇÃO DE NÍVEIS DE MCP1 COM CÂNCER
#=====================================
def analyse_mcp_cancer(df):
    df['class_mcp_num'] =df['classificacao_mcp'].replace({'Normal':0, 'Moderado':1, 'Alto':2}) 
    return df.groupby('cancer')['class_mcp_num'].value_counts(normalize = True) * 100
    