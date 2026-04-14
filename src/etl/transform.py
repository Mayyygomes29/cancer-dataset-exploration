from scipy import stats

# =========================
# TRANSFORM
# =========================
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