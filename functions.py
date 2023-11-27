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

def UserForGenre(genero:str):
    consulta2 = pd.read_csv('UserForGenre.csv')
    
    # Filtrar el DataFrame por el género dado
    genre_data = consulta2[consulta2['genres'] == genero]

    # Encontrar al usuario con más horas jugadas para ese género
    top_user = genre_data.loc[genre_data['hours_game'].idxmax()]['user_id']

    # Crear una lista de acumulación de horas jugadas por año
    hours_by_year = genre_data.groupby('year')['hours_game'].sum().reset_index()
    hours_by_year = hours_by_year.rename(columns={'year': 'Año', 'hours_game': 'Horas'})
    # Convertir las horas a enteros (int) dividiendo por 60
    #hours_by_year['Horas'] = (hours_by_year['Horas'] / 60).astype(int)
    hours_list = hours_by_year.to_dict(orient='records')

    # Crear el diccionario de retorno
    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): top_user,
        "Horas jugadas": hours_list
    }

    return result


def PlayTimeGenre(genero: str):
    result_df = pd.read_csv('PlayTimeGenre.csv')

    # Filtrar el DataFrame para el género específico
    filtered_df = result_df[result_df['genres'] == genero]
    
    # Agrupar por año de lanzamiento y sumar las horas jugadas
    grouped_df = filtered_df.groupby('year')['hours_game'].sum()
    
    # Encontrar el año con más horas jugadas
    max_hours_year = grouped_df.idxmax()

    # Construye el response_data
    response_data = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_hours_year)}

    # Muestra el resultado
    return response_data


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

# In[ ]:
def recomendacion_usuario(item_id):
    df = pd.read_csv('modelo_espec.csv')

    # Filtrar el DataFrame por el año especificado
    result_df = df[df['item_id'] == item_id]
    
    response_data = result_df['RecomendacionesTop5']
    '''
    response_data = [{"Puesto 1": result_df.iloc[0]['developer']},
                    {"Puesto 2": result_df.iloc[1]['developer']},
                    {"Puesto 3": result_df.iloc[2]['developer']}]
    '''
    return response_data