from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

#==================================
# Métricas do modelo
#==================================
def metrics_model(y_test, previsao):
    return {'accuracy': accuracy_score(y_test, previsao),
            'precision': precision_score(y_test, previsao),
            'recall': recall_score(y_test, previsao),
            'confusion_matrix': confusion_matrix(y_test, previsao),
            'classification_report': classification_report(y_test, previsao)}