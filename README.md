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
*Transformaciones de Datos:* Realicé transformaciones necesarias para leer los datasets con el formato correcto, siempre con el objetivo de optimizar el rendimiento de la API y el entrenamiento del modelo. <br />
*Feature Engineering:* Creé la columna 'sentiment_analysis' aplicando análisis de sentimiento a las reseñas de los usuarios. <br />
*Desarrollo de API:* Implementé una API con FastAPI y Render que proporciona consultas sobre información de videojuegos. <br />

**2. Análisis Exploratorio de Datos (EDA)** <br />
Investigé relaciones entre variables, identifiqué outliers y busqué patrones interesantes en los datos.<br />

**3. Modelos de Aprendizaje Automático** <br />
*Sistema de Recomendación ítem-ítem:* Desarrollé un modelo que recomienda juegos similares en base a un juego dado, utilizando similitud del coseno. <br />
*Sistema de Recomendación usuario-ítem:* Implementé un modelo que recomienda juegos a un usuario en función de juegos que otros usuarios similares disfrutaron.<br />

**4. Implementación de MLOps** <br />
*Deploy del Modelo:* Desplegué el modelo de recomendación como parte de la API, permitiendo consultas en tiempo real. <br />

**5. Video Explicativo** <br />
Grabé un video explicativo que muestra el funcionamiento de la API, consultas realizadas y una breve explicación de los modelos de ML utilizados.<br />
<br />

## Estructura del Repositorio <br />
**1. [/Notebooks](Notebooks/):** Contiene los Jupyter Notebooks donde se realizaron las extracciones, transformaciones y carga de datos (ETL) y análisis exploratorio de los datos (EDA).<br />

**2. [/API](API/):** Almacena el código correspondiente a la implementación de la API con FastAPI.<br />

**3. [/Modelos](Modelos/):** Contiene el código y los resultados de los modelos de recomendación implementados.<br />

**4. [/Datos](Datasets/):** Almacena los datasets utilizados y, si es posible, una versión limpia y procesada de los mismos.<br />

**4. [/Video](Video/):** Contiene el video explicativo del proyecto.<br />

