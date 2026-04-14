from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from src.evaluation.metrics import metrics_model


#========================
#CLASSIFICAÇÃO
#========================
def model_classification(df):
    df['cancer'] = df['Classificacao']
    df['cancer']= df['cancer'].replace({2:1, 1:0})

    x = df[['leptina_zs','imc_zs','idade_zs','glicose_zs','insulina_zs',
            'homa_zs','adiponectina_zs','resistina_zs']]
    y = df['cancer']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,
                                                        stratify=y,
                                                        random_state=42)

    model = LogisticRegression(random_state=42)

    model.fit(x_train, y_train)
    previsao = model.predict(x_test)
    y_prob = model.predict_proba(x_test)[:,1]
    metrics = metrics_model(y_test, previsao)
    
    df_resultado = x_test.copy()
    df_resultado['real'] = y_test.values
    df_resultado['previsto'] = previsao
    df_resultado['probabilidade'] = y_prob

    return {'model': model,
            'previsao': previsao,
            'metrics': metrics,
            'y_prob': y_prob,
            'df_result': df_resultado}


#==========================
#CLUSTERING
#==========================
def model_cluster(df):
    x = df[['idade_zs', 'imc_zs',
       'glicose_zs', 'insulina_zs', 'homa_zs', 'leptina_zs', 'adiponectina_zs',
       'resistina_zs']]
    kmeans = KMeans(n_clusters=4,random_state=42 )
    df['cluster'] = kmeans.fit_predict(x)
    return df, kmeans
    
    