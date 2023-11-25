#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI, HTTPException 
import traceback  # Importa la biblioteca para imprimir la traza de la pila
from typing import List, Dict
import pandas as pd
#import pyarrow
from functions import UsersRecommend
from functions import sentiment_analysis
from functions import UsersWorstDeveloper
from functions import PlayTimeGenre


# In[ ]:


# Crea una instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"Mensaje": "Proyecto Individual"}


# In[ ]:

@app.get("/PlayTimeGenre/{genero}")
async def user(genero: str):
    try:
        result = PlayTimeGenre(genero)
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo PlayTimeGenre.csv: {str(e)}")

    except Exception as e:
        traceback.print_exc()  # Imprime la traza de la pila
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

# In[ ]:


@app.get("/UsersRecommend/{year}")
async def user(year: str):
    try:
        year = int(year)
        
        result = UsersRecommend(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")

# In[ ]:


@app.get("/UsersWorstDeveloper/{year}")
async def user(year: str):
    try:
        year = int(year)

        result = UsersWorstDeveloper(year)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")

# In[ ]:


@app.get("/sentiment_analysis/{empresa_desarrolladora}")
async def user(empresa_desarrolladora: str):
    try:
        result = sentiment_analysis(empresa_desarrolladora)
        
        return result
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UsersRecommend.csv: {str(e)}")
