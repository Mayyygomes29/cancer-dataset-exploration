#===========================
#CARREGAMENTO
#============================
def load(df):
    return df.to_csv('data/processed/dados_tratado.csv', index=False)  