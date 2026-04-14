from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import seaborn.objects as so


#===========================
#GRÁFICO BARRA
#===========================
def plot_bar(contagem, titulo, cor):
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(contagem.index, contagem.values, width=0.30, color=cor)

    ax.set_title(titulo)
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Quantidade')

    ax.bar_label(ax.containers[0])

    return fig


#==============================
#GRÁFICO CORRELAÇÃO
#==============================
def plot_correlation(corr, texto):
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(
        corr,
        annot=True,       
        fmt=".2f",         
        cmap='viridis',   
        linewidths=0.5,
        ax=ax
    )
    ax.set_title(texto)
    return fig


#==============================
#GRÁFICO DE DISPERSÃO
#==============================
def plot_disper(df, x, y, hue, titulo):
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(7, 6))

    sns.scatterplot(
        data=df,
        x=x,       
        y=y,    
        hue=hue,  
        palette="tab10",
        ax=ax
    )

    ax.set_title(titulo)
    ax.set_xlabel(x)
    ax.set_ylabel(y)

    return f