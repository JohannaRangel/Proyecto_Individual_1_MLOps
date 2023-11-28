![Steam](https://github.com/JohannaRangel/Proyecto_Individual_1_MLOps/raw/main/assets/steam.png)
<br />
# Proyecto MLOps: Sistema de Recomendación de Videojuegos para Usuarios de Steam

### Descripción del Proyecto
Este proyecto representa una pieza clave de la fase de LABS en el bootcamp de Henry, donde se enfoca en la práctica de habilidades técnicas y soft skills necesarias en el mercado laboral. Se desarrolló un caso de negocio real utilizando conjuntos de datos públicos de la industria de videojuegos, específicamente de la renombrada plataforma en línea STEAM.

### Objetivo
El propósito central es la creación del primer modelo de Machine Learning (end to end) que resuelva un problema de negocio en Steam, a través de un enfoque que involucra tareas de Data Engineering (ETL, EDA, API) hasta la implementación del ML. Se busca lograr un rápido desarrollo y tener un Producto Mínimo Viable (MVP).<br />
<br />

## Etapas del Proyecto <br />
![Etapas](https://github.com/JohannaRangel/Proyecto_Individual_1_MLOps/raw/main/assets/Etapas.png)  
<br />
**1. Ingeniería de Datos (ETL y API)** <br />

- **1.1 *Transformaciones de Datos:*** Inicialmente, recibí tres (3) archivos en formato JSON, los cuales están almacenados en la carpeta **Input** de un repositorio público en **[Google Drive](https://bit.ly/47J98PN).** Realicé transformaciones esenciales para cargar los conjuntos de datos con el formato adecuado. Estas transformaciones se llevaron a cabo con el propósito de optimizar tanto el rendimiento de la API como el entrenamiento del modelo.<br />
  + [australian_user_reviews.json](https://bit.ly/49LHpQo): Contiene las reseñas de juegos específicamente realizadas por usuarios australianos. Se puede hacer referencia al notebook [ETL_user_reviews](Notebooks/ETL_user_reviews.ipynb) para obtener más detalles sobre cómo se procesaron las reseñas dando como resultado un nuevo archivo con datos limpios, [user_reviews_cleaned.csv](Datasets/Archivos_Limpios/user_reviews_cleaned.csv).<br />
  + [output_steam_games.json](https://bit.ly/49MGNKk): Este archivo proporciona información detallada sobre los juegos disponibles en la plataforma Steam. Incluye datos como géneros, etiquetas, especificaciones, desarrolladores, año de lanzamiento, precio y otros atributos relevantes de cada juego. En el notebook [ETL_steam_game](Notebooks/ETL_steam_game.ipynb) puedes revisar el proceso de limpieza y transformación de datos, el cual culmina con la creación de un nuevo archivo llamado [steam_games_cleaned.csv](Datasets/Archivos_Limpios/steam_games_cleaned.csv). <br /> 
  + [australian_users_items.json](https://bit.ly/46AauM0): El archivo australian_users_items.json contiene información sobre los ítems relacionados con usuarios australianos. Este conjunto de datos ha pasado por un proceso de Extracción, Transformación y Carga (ETL), que se detalla en el notebook [ETL_user_items](Notebooks/ETL_user_items.ipynb). Como resultado de este proceso, se generó un nuevo archivo [user_items_cleaned.csv](Datasets/Archivos_Limpios/user_items_cleaned.csv) para facilitar su manipulación y análisis, brindando así una estructura más amigable y lista para su integración en el modelo.<br />
  
- **1.2 *Feature Engineering:*** Creé la columna **``` sentiment_analysis ```** aplicando análisis de sentimiento a las reseñas de los usuarios, puede ver el detalle en el notebook [ETL_user_reviews](Notebooks/ETL_user_reviews.ipynb). <br />

- **1.3 *Desarrollo de API:*** Implementé una API con FastAPI y se deployó en Render, ésta proporciona cinco (5) consultas sobre información de videojuegos. Puede ver el detalle del código en los notebooks [Funciones](Notebooks/Funciones.ipynb) y [Consultas](Consultas/Funciones.ipynb).<br />
  + Endpoint 1 (PlayTimeGenre): Devuelve año con mas horas jugadas para un género dado.<br />
  + Endpoint 2 (UserForGenre): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.<br />
  + Endpoint 3 (UsersRecommend): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.<br />
  + Endpoint 4 (UsersWorstDeveloper): Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.<br />
  + Endpoint 5 (sentiment_analysis): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor
Para acceder a la funcionalidad completa de la API y explorar las recomendaciones de juegos, puedes visitar [URL de la API]([Consultas](https://proyecto-individual-1-mlops-9770.onrender.com/docs)). En este sitio, encontrarás diversas funciones, desde obtener las mejores recomendaciones de juegos hasta explorar análisis de sentimientos y estadísticas detalladas. ¡Disfruta explorando el mundo de los juegos con nuestra API <br />
  
**2. Análisis Exploratorio de Datos (EDA)** <br />
Investigé relaciones entre variables, identifiqué outliers y busqué patrones interesantes en los datos.<br />

**3. Modelos de Aprendizaje Automático** <br />
- *Sistema de Recomendación ítem-ítem:* Desarrollé un modelo que recomienda juegos similares en base a un juego dado, utilizando similitud del coseno. <br />
- *Sistema de Recomendación usuario-ítem:* Implementé un modelo que recomienda juegos a un usuario en función de juegos que otros usuarios similares disfrutaron.<br />

**4. Implementación de MLOps** <br />
*Deploy del Modelo:* Desplegué el modelo de recomendación como parte de la API. <br />

**5. Video Explicativo** <br />
Grabé un video explicativo que muestra el funcionamiento de la API, consultas realizadas y una breve explicación de los modelos de ML utilizados.<br />
<br />

## Estructura del Repositorio <br />
**1. [/Notebooks](Notebooks/):** Contiene los Jupyter Notebooks donde se realizaron las extracciones, transformaciones y carga de datos (ETL) y análisis exploratorio de los datos (EDA).<br />

**2. [/API](API/):** Almacena el código correspondiente a la implementación de la API con FastAPI.<br />

**3. [/Modelos](Modelos/):** Contiene el código y los resultados de los modelos de recomendación implementados.<br />

**4. [/Datasets](Datasets/):** Almacena los datasets utilizados en una versión limpia y procesada de los mismos.<br />

**5. [/Video](Video/):** Contiene el video explicativo del proyecto.<br />
<br />

## Ejecutar la API (en su máquina local) <br />
1. Clonar el repositorio <br />
```
git@github.com:JohannaRangel/Proyecto_Individual_1_MLOps.git
```
2. Crear entorno virtual<br />
```
python3 -m venv <nombre_del_entonto>
```
3. Vaya al directorio del entorno virtual y actívelo<br />
- 3.1. Para Windows:
```
Scripts/activate
```
- 3.2. Para Linux/Mac:
```
bin/activate
```
4. Instalar los requerimientos<br />
```
pip install -r requirements.txt
```
5. Ejecute la API con uvicorn<br />
```
uvicorn main:app --reload
```
