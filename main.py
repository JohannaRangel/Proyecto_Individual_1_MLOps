#!/usr/bin/env python
# coding: utf-8

# En este notebook está el código que 

# ### Librerías

# In[ ]:


from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback  
from typing import List, Dict
import pandas as pd
from functions import UsersRecommend, sentiment_analysis, UsersWorstDeveloper, PlayTimeGenre, UserForGenre, recomendacion_usuario


# ### Instancia

# In[ ]:


# Crea una instancia de la aplicación FastAPI
app = FastAPI()


# ### Root

# In[ ]:


@app.get("/")
async def root():
    """
    Proyecto FastAPI - Sistema de Recomendaciones

    Versión: 1.0.0

    ---

    """
    return {"Mensaje": "Proyecto Individual N° 1 - Johanna Rangel"}


# ### Endpoint 1

# In[ ]:


@app.get("/PlayTimeGenre/{genero}", tags=['PlayTimeGenre'])
async def endpoint1(genero: str):
    """
    Descripción: Retorna el año con más horas jugadas para un género dado.
    
    Parámetros:
        - genero (str): Género para el cual se busca el año con más horas jugadas. Debe ser un string, ejemplo: Action
    
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género Action" : 2012}
    """
    try:
        # Validación adicional para asegurarse de que el género no sea nulo o esté vacío
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = PlayTimeGenre(genero)
    
        # Validación para verificar si el género existe en los datos
        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")

        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo PlayTimeGenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# ### Endpoint 2

# In[ ]:


@app.get("/UserForGenre/{genero}", tags=['UserForGenre'])
async def endpoint2(genero: str):
    """
    Descripción: Retorna el usuario que acumula más horas jugadas para un género dado y una lista de la acumulación de horas jugadas por año.

    Parámetros:
        - genero (str): Género para el cual se busca el usuario con más horas jugadas. Debe ser un string, ejemplo: Adventure

    Ejemplo de retorno: {"Usuario con más horas jugadas para Género Adventure": Evilutional, Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
    """
    try:
        # Validación adicional para asegurarse de que el género no sea nulo o esté vacío
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = UserForGenre(genero)
        
        # Validación para verificar si el género existe en los datos
        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")
            
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UserForGenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# ### Endpoint 3

# In[ ]:


@app.get("/UsersRecommend/{year}", tags=['UsersRecommend'])
async def endpoint3(year: str):
    """
    Descripción: Retorna el top 3 de juegos MÁS recomendados por usuarios para el año dado.
    
    Parámetros:
        - year (str): Año para el cual se busca el top 3 de juegos más recomendados.Debe ser número de 4 digitos, ejemplo: 2015

    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    try:
        year = int(year)
    
        if not (2000 <= year <= 2100):
            error_message = f"El año debe estar en el rango entre 2000 y 2100 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})
        
        result = UsersRecommend(year)
    
        if result:
            return result
        else:
            #raise HTTPException(status_code=404, detail=f"No se encontraron recomendaciones para el año {year}.")
            error_message = "No se encontraron recomendaciones para el año {year} {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

    except FileNotFoundError as e:
        error_message = f"Error al cargar el archivo UsersRecommend.csv: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})

    except Exception as e:
        error_message = f"Error interno del servidor: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})



# ### Endpoint 4

# In[ ]:


@app.get("/UsersWorstDeveloper/{year}", tags=['UsersWorstDeveloper'])
async def endpoint4(year: str):
    """
    Descripción: Retorna el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.
    
    Parámetros:
        - year (str): Año para el cual se busca el top 3 de desarrolladoras menos recomendadas. Debe ser número de 4 digitos, ejemplo: 2015


    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    try:
        year = int(year)
        result = UsersWorstDeveloper(year)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersWorstDeveloper.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# ### Endpoint 5

# In[ ]:


@app.get("/sentiment_analysis/{empresa_desarrolladora}", tags=['sentiment_analysis'])
async def enpoint5(empresa_desarrolladora: str):
    """
    Descripción: Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
    
    Parámetros:
        - empresa_desarrolladora (str): Nombre de la empresa desarrolladora para la cual se realiza el análisis de sentimiento. Debe ser un string, ejemplo: Valve
    
    Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
    """
    try:
        result = sentiment_analysis(empresa_desarrolladora)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo sentiment_analysis.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


# ### Sistema de recomendación item-item

# In[ ]:


@app.get("/recomendacion_usuario/{item_id}", tags=['recomendacion_usuario item_item'])
async def item(item_id: int):
    """
    Descripción: Ingresando el id de producto, devuelve una lista con 5 juegos recomendados similares al ingresado.
    
    Parámetros:
        - item_id (str): Id del producto para el cual se busca la recomendación. Debe ser un número, ejemplo: 761140
        
    Ejemplo de retorno: "['弹炸人2222', 'Uncanny Islands', 'Beach Rules', 'Planetarium 2 - Zen Odyssey', 'The Warrior Of Treasures']"

    """
    try:
        item_id = int(item_id) 
        resultado= recomendacion_usuario(item_id)
        return resultado
    except Exception as e:
        return {"error":str(e)}

