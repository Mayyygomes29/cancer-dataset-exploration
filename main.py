import pandas as pd

from src.analysis.eda import variable_correlation,analyse_age_cancer, analyse_qnt_cancer
from src.analysis.eda import analyse_cluster,analyse_mean_variable_cluster
from src.analysis.eda import analyse_contig, analyse_mean_variable_cancer,analyse_mcp_cancer, analyse_classification

from src.etl.extract import extract
from src.etl.load import load
from src.etl.transform import transform

from src.features.feature_engineering import create_glicose_class, create_insulin_class, create_mcp_class,normalization

from src.model.train import model_classification, model_cluster


def run_pipeline():
    dados = extract()
    df = transform(dados)
    return df  


def main():
    df = run_pipeline()
    df =create_glicose_class(df)
    df = create_insulin_class(df)
    df = create_mcp_class(df)
    classificacao_mcp = analyse_classification(df, 'classificacao_mcp')
    classificacao_insulina = analyse_classification(df,'classificacao_insulina')
    classificacao_glicose = analyse_classification(df,'classificacao_glicose')
    correlacao_variaveis = variable_correlation(df)
    normalization(df)

    classificacao = model_classification(df)
    cluster = model_cluster(df)

    media_idade_cancer= analyse_age_cancer(df)
    qnt_cancer  = analyse_qnt_cancer(df)
    qnt_cluster = analyse_cluster(df)   
    medias_variaveis_cluster= analyse_mean_variable_cluster(df)
    media_variaveis_cancer= analyse_mean_variable_cancer(df)
    mcp_cancer = analyse_mcp_cancer(df)
    contigencia = analyse_contig(df)
    
    
    return {'df': df,
            'classificacao': classificacao,
            'cluster' : cluster,
            'media_idade_cancer':media_idade_cancer,
            'qnt_cancer':qnt_cancer,
            'qnt_cluster': qnt_cluster,
            'medias_variaveis_cluster': medias_variaveis_cluster,
            'media_variaveis_cancer': media_variaveis_cancer,
            'mcp_cancer' :  mcp_cancer,
            'classificacao_mcp': classificacao_mcp,
            'classificacao_insulina': classificacao_insulina,
            'classificacao_glicose': classificacao_glicose,
            'correlacao_variaveis':correlacao_variaveis,
            'contigencia': contigencia
            }


if __name__ == "__main__":
    main()