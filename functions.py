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


def PlayTimeGenre(genero: str):
    df = pd.read_csv('PlayTimeGenre.csv')
    
    # Filtrar el DataFrame por el año especificado
    result_df = df[df['genres'] == genero]
    
    response_data = {f'Año de lanzamiento con más horas jugadas para {row["genres"]}': row["year"] for _, row in result_df.iterrows()}

    return response_data
# In[4]:


def UsersRecommend(year: int):
    df = pd.read_csv('UsersRecommend.csv')
    
    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]

    response_data = [{"Puesto 1": result_df.iloc[0]['name']},
                     {"Puesto 2": result_df.iloc[1]['name']},
                     {"Puesto 3": result_df.iloc[2]['name']}]

    return response_data


# In[4]:
def UsersWorstDeveloper(year: int):
    df = pd.read_csv('UsersWorstDeveloper.csv')

    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]
    
    response_data = [{"Puesto 1": result_df.iloc[0]['developer']},
                    {"Puesto 2": result_df.iloc[1]['developer']},
                    {"Puesto 3": result_df.iloc[2]['developer']}]
    
    return response_data


# In[ ]:
def sentiment_analysis(empresa_desarrolladora: str):
    df = pd.read_csv('sentiment_analysis.csv')

    # Filtrar por la empresa desarrolladora
    result_df = df[df['developer'] == empresa_desarrolladora]

    # Convertir a formato de diccionario
    response_data = result_df.set_index('developer').to_dict(orient='index')
    
    return response_data