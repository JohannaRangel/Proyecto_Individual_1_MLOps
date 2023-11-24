#!/usr/bin/env python
# coding: utf-8

# # Función UsersRecommend

# En esta sección, me enfocaré en perfeccionar las consultas que consumirá la API utilizando los archivos generados en los informes ETL. El objetivo es optimizar éstas consultas para que sean eficientes y livianas, asegurando su rapidez y eficacia.

# ### Importación de Bibliotecas

# In[1]:


import pandas as pd
import os

# ### Cargar el conjunto de datos limpiado

# La versión de los archivos ya tratados y limpiados que se utilizaran en esta etapa se encuentran almacenados en Google Drive con acceso compartido. Datasets: https://bit.ly/47J98PN

# Fuente de datos: 
# - user_reviews_cleaned.cvs
# - steam_games_cleaned.csv

# ### Rutinas

# def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
# 

# ### Pruebas

# In[4]:


def UsersRecommend(year: int):
    df = pd.read_csv('UsersRecommend.csv')
    
    # Filtrar el DataFrame por el año especificado
    top3_games = df[df['year'] == year]

    response_data = [{"Puesto 1": top3_games.iloc[0]['name']},
                    {"Puesto 2": top3_games.iloc[1]['name']},
                    {"Puesto 3": top3_games.iloc[2]['name']}]

    return response_data


# In[4]:
def UsersWorstDeveloper(year: str):
    df_steam_games = pd.read_csv('steam_games_cleaned.csv')
    df_user_reviews = pd.read_csv('user_reviews_cleaned.csv')
    
    # Unir los DataFrames
    df_merged = pd.merge(df_user_reviews, df_steam_games, on='item_id', how='left')

    # Filtrar las filas que cumplen con las condiciones
    df_filtered = df_merged.loc[(df_merged['recommend'] == False) & (df_merged['sentiment_analysis'] == 0),
                                ['year_x', 'developer']]
 
    # Renombrar la columna 'year_x' a 'year'
    df_filtered = df_filtered.rename(columns={'year_x': 'year'})

    # Contar las ocurrencias de cada desarrolladora por año
    developer_counts = df_filtered.groupby(['year', 'developer']).size().reset_index(name='count')
    
    # Ordenar por 'year' y 'count' en orden descendente
    grouped_result = developer_counts.sort_values(by=['year', 'count'], ascending=[False, False])    

    # Obtener el top 3 por año
    top3_by_year = grouped_result.groupby('year').head(3)    
    
    response_data = [{"Puesto 1": top3_by_year.iloc[0]['developer']},
                    {"Puesto 2": top3_by_year.iloc[1]['developer']},
                    {"Puesto 3": top3_by_year.iloc[2]['developer']}]
    
    return response_data


# In[ ]:
def sentiment_analysis(empresa_desarrolladora: str):
    df_steam_games = pd.read_csv('steam_games_cleaned.csv')
    df_user_reviews = pd.read_csv('user_reviews_cleaned.csv')

    # Unir los DataFrames por la columna 'item_id'
    merged_df = pd.merge(df_steam_games, df_user_reviews, on='item_id', how='inner')

    # Agrupar por desarrolladora y sentimiento, y contar las ocurrencias
    result_df = merged_df.groupby(['developer', 'sentiment_analysis']).size().reset_index(name='count')

    # Pivoteando el DataFrame para tener sentimientos como columnas
    result_df = result_df.pivot(index='developer', columns='sentiment_analysis', values='count').reset_index()

    # Renombrar las columnas según el formato deseado
    result_df.columns = ['developer', 'Negative', 'Neutral', 'Positive']

    # Rellenar NaN con 0
    result_df = result_df.fillna(0)

    # Convertir las columnas a tipo int
    result_df[['Negative', 'Neutral', 'Positive']] = result_df[['Negative', 'Neutral', 'Positive']].astype(int)

    # Filtrar por la empresa desarrolladora
    df_filtered = result_df[result_df['developer'] == empresa_desarrolladora]

    # Convertir a formato de diccionario
    sentiment_dict = df_filtered.set_index('developer').to_dict(orient='index')

    return sentiment_dict