from scipy import stats


# =========================
# INSULINA 
# =========================
def create_insulin_class(df):   
    df = df.copy()
    def classificar_insulina(valor):
        if valor < 2:
            return 'Baixa'
        elif valor <= 25:
            return 'Normal'
        else:
            return 'Alta'

    df['classificacao_insulina'] = df['Insulina'].apply(classificar_insulina)

    return df
    

# =========================
# GLICOSE
# =========================
def create_glicose_class(df):
    df = df.copy()
    def classificar_glicose(valor):
        if valor < 100:
            return 'Normal'
        elif valor <= 125:
            return 'Pré-Diabete'
        else:
            return 'Diabete'

    df['classificacao_glicose'] = df['Glicose'].apply(classificar_glicose)
    return df


# =========================
# MCP1
# =========================
def create_mcp_class(df):
    df = df.copy()
    def classificar_mcp(valor):
        if valor <= 200:
            return 'Normal'
        elif valor <= 400:
            return 'Moderado'
        else:
            return 'Alto'

    df['classificacao_mcp'] = df['MCP1'].apply(classificar_mcp)

    return df



#=================================
# NORMALIZANDO
#=================================
def normalization(df):
    colunas = [
        'Idade', 'IMC', 'Glicose', 'Insulina',
        'HOMA', 'Leptina', 'Adiponectina',
        'Resistina', 'MCP1'
    ]

    for col in colunas:
        if col in df.columns:
            df[f'{col.lower()}_zs'] = stats.zscore(df[col]).round(2)
        else:
            print(f"Coluna '{col}' não encontrada")

    return df