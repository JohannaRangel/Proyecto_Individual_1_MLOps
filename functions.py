#!/usr/bin/env python
# coding: utf-8

# ### Funciones para Endpoints / ML

# En esta sección, nos centraremos en consumir los archivos que se generaron en el notebook **Consultas**. que serán utilizadas por la API. El objetivo principal es dar respuestas a los Endpoints y a los Modelos Machine Learning, garantizando rapidez y eficacia en la ejecución de la API.

# In[6]:


import pandas as pd
import os


# ### Endpoint 1

# **def PlayTimeGenre( genero : str ):** Debe devolver año con mas horas jugadas para dicho género.
# 
# Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
# 
# Input: **PlayTimeGenre.csv**

# In[ ]:


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


# ### Endpoint 2

# **def UserForGenre( genero : str ):** Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
# 
# Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
# 
# Input: **UserForGenre.csv**

# In[ ]:


def UserForGenre(genero:str):
    consulta2 = pd.read_csv('UserForGenre.csv')
    
    # Filtrar el DataFrame por el género dado
    genre_data = consulta2[consulta2['genres'] == genero]

    # Encontrar al usuario con más horas jugadas para ese género
    top_user = genre_data.loc[genre_data['hours_game'].idxmax()]['user_id']

    # Crear una lista de acumulación de horas jugadas por año
    hours_by_year = genre_data.groupby('year')['hours_game'].sum().reset_index()
  
    hours_by_year = hours_by_year.rename(columns={'year': 'Año', 'hours_game': 'Horas'})
    
    hours_list = hours_by_year.to_dict(orient='records')

    # Crear el diccionario de retorno
    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): top_user,
        "Horas jugadas": hours_list
    }

    return result


# ### Endpoint 3

# **def UsersRecommend( año : int )**: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
# 
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
# 
# Input: **UsersRecommend.csv**

# In[ ]:


def UsersRecommend(year: int):
    df = pd.read_csv('UsersRecommend.csv')
    
    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]

    response_data = [{"Puesto 1": result_df.iloc[0]['name']},
                     {"Puesto 2": result_df.iloc[1]['name']},
                     {"Puesto 3": result_df.iloc[2]['name']}]

    return response_data


# ### Endpoint 4

# **def UsersWorstDeveloper( año : int )**: Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
# 
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
# 
# Input: **UsersWorstDeveloper.csv**

# In[ ]:


def UsersWorstDeveloper(year: int):
    df = pd.read_csv('UsersWorstDeveloper.csv')

    # Filtrar el DataFrame por el año especificado
    result_df = df[df['year'] == year]
    
    response_data = [{"Puesto 1": result_df.iloc[0]['developer']},
                    {"Puesto 2": result_df.iloc[1]['developer']},
                    {"Puesto 3": result_df.iloc[2]['developer']}]
    
    return response_data



# ### Endpoint 5

# **def sentiment_analysis( empresa desarrolladora : str )**: Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
# 
# Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
# 
# Input: **sentiment_analysis.csv**

# In[ ]:


def sentiment_analysis(empresa_desarrolladora: str):
    df = pd.read_csv('sentiment_analysis.csv')

    # Filtrar por la empresa desarrolladora
    result_df = df[df['developer'] == empresa_desarrolladora]

    # Convertir a formato de diccionario
    response_data = result_df.set_index('developer').to_dict(orient='index')
    
    return response_data


# ### ML

# ### Recomendación item-item

# In[7]:


def recomendacion_usuario(item_id):
    df = pd.read_csv('recomienda_item_item.csv')
    
    # Filtrar el DataFrame por el año especificado
    result_df = df[df['item_id'] == item_id]
    
    response_data = result_df['Recomendaciones']
 
    return response_data


# In[ ]:




