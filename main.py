#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI, HTTPException 
from typing import List, Dict
import pandas as pd
#import pyarrow
from functions import UsersRecommend
from functions import sentiment_analysis
from functions import UsersWorstDeveloper


# In[ ]:


# Crea una instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"Mensaje": "Proyecto Individual"}

# ### Endpoint para obtener el top 3 de juegos MÁS recomendados por usuarios para el año dado

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
