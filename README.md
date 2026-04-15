# Análise de Dados e Machine Learning - Indicadores de Câncer

## Sobre o Projeto
Este projeto tem como objetivo analisar dados clínicos relacionados ao câncer, utilizando técnicas de análise exploratória de dados (EDA), engenharia de atributos, visualização e modelos de Machine Learning.

A aplicação foi desenvolvida com Streamlit, permitindo a exploração interativa dos dados, identificação de padrões e análise preditiva da presença de câncer.

---

## Objetivos

- Explorar dados clínicos e identificar padrões
- Criar variáveis interpretáveis com base em critérios médicos
- Aplicar modelos de Machine Learning
- Visualizar dados de forma interativa
- Construir um dashboard funcional para análise

---

## Pipeline de Dados

### Extração (Extract)

```python
def extract():
    path = os.path.join("data", "dataR2.csv")
    return pd.read_csv(path)
```
### Transformação (transform)
```python
def transform(df):
    #RENAME
    df = df.rename(columns={
        'Age':'Idade',
        'BMI':'IMC', 
        'Glucose':'Glicose',
        'Insulin':'Insulina',
        'Leptin':'Leptina',
        'Adiponectin':'Adiponectina',
        'Resistin':'Resistina',
        'Classification': 'Classificacao',
        'MCP.1': 'MCP1'
        }).round(2)

    #INDEX
    df.index.name = 'ID'

    #IDENTIFICANDO VALORES NULOS
    print(df.isna().sum())

    return df
```
### Carregar (Load)
```python
def load(df):
    return df.to_csv('data/processed/dados_tratado.csv', index=False)  
```
## Transformação (Feature Engineering)

Criação de variáveis categóricas com base em regras clínicas:

### Insulina

Baixa (< 2)
Normal (2 – 25)
Alta (> 25)

### Glicose

Normal (< 100)
Pré-Diabete (100 – 125)
Diabete (> 125)

### MCP-1

Normal (≤ 200)
Moderado (≤ 400)
Alto (> 400)

### Normalização
Aplicação de padronização com Z-score nas variáveis:

- Idade
- IMC
- Glicose
- Insulina
- HOMA
- Leptina
- Adiponectina
- Resistina
- MCP1
  
## Análise Exploratória de Dados (EDA)

Foram realizadas análises como:

- Distribuição de variáveis categóricas
- Correlação entre variáveis clínicas
- Contagem de pacientes com e sem câncer
- Média de idade por grupo
- Comparação de variáveis entre grupos
  
### Técnicas utilizadas:
- value_counts()
- groupby()
- crosstab()

## Visualização de Dados
- Gráficos de barras
- Heatmap de correlação
- Gráficos de dispersão
  
## Modelagem
### Classificação (Supervisionado)

Modelo: Regressão Logística

Separação treino/teste (80/20)
Estratificação da variável alvo
Previsões e probabilidades

### Clusterização (Não Supervisionado)

Modelo: K-Means

Número de clusters: 4
Segmentação de pacientes

## Métricas
- Acurácia
- Precisão
- Recall
- F1-score
  
## Interface da Aplicação

A aplicação foi construída com Streamlit e organizada em páginas:

- Home
- EDA
- Análise de Modelos
- Métricas

## Tecnologias Utilizadas
- Python
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
  
```
Estrutura do Projeto
cancer/
│
│── data/
│   └── dataR2.csv
│
├── src/
│    ├── etl/
│   |       extract.py
│   |       transform.py
│   |       load.py
│   ├── analysis/
|   |       eda.py
|   ├── features/
|   |       feature_engineering.py
│   ├── model/
|   |       train.py
│   ├── visualization/
│   │        graphs.py
│   ├── evaluation/
│   |        metrics.py
│
│── streamlit_app.py
|
├── requirements.txt
└── README.md
```
## Fonte dos Dados

Os dados utilizados neste projeto foram obtidos no:

- UCI Machine Learning Repository  
- Dataset: Breast Cancer Coimbra  

🔗 https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra

Este dataset contém informações clínicas de pacientes, incluindo variáveis metabólicas e inflamatórias utilizadas para análise e modelagem.

## Como executar
```
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

pip install -r requirements.txt
streamlit run app/app.py
````
## Deploy

  [Link para acessar o streamlit](https://cancer-dataset-exploration.streamlit.app/page_metrics)


## Melhorias Futuras
- Random Forest / XGBoost
- Ajuste de hiperparâmetros
- Pipeline automatizado
- API com FastAPI

## Autora
### Mayara Gomes Silva
Data Science | Python | Machine Learning 

##### Objetivo

Projeto desenvolvido para prática de análise de dados e construção de portfólio.
