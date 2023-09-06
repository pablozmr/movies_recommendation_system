# Sistema de recomendacion de peliculas
Hola! Este es un proyecto en el cual empleamos herramientas de machine learning para brindar una recomendacion segun la pelicula que el usuario elija. Ademas tiene algunas funciones para adquirir informacion acerca de las peliculas, productoras, directores y algunas cosas mas. 
<img src=https://github.com/pablozmr/movies_recommendation_system/blob/main/images/movies_recomendacion.png>

## Requerimientos del proyecto:
Para poder trabajar con los datos de forma deseada, lo primero que debemos hacer es ver la calidad de los datos en los datasets que disponemos, luego manipularlos de tal forma que nos sean utiles. Para la transformacion de los datos utilizamos las librerias Pandas y Numpy de python.
Para el entrenamiento del modelo de machine learning usamos las librerias sklearn, nltk y el modulo cosine_similarity.
Para su deployment empleamos streamlit, streamlit_folium, requests y PIL.

Estructura de contenido

1. informe.html: Este archivo guarda el EDA generado con pandas.profiling.
2. main_streamlit.py: Archivo de Python que usamos para ejecutar la aplicacion en Streamlit.
3. data:
-movies_credits.csv: Este archivo es el dataset limpio para aplicar las funciones.
-movies_recomendacion.csv: Este archivo es el dataset para aplicar el sistema de recomendacion.
-primer_similarity.pkl / segundo_similarity.pkl: Estos archivos son el array de arrays que devuelve el entrenamiento del modelo de machine learning que luego se concatenan en main_streamlit.py ya que pensan mas de 25mbs juntos y github no permite archivos pesados.
-movies_dict.pkl: Este archivo sirve para poder tener a disposicion los titulos y la info de las peliculas en los selectbox de streamlit.
5. notebooks:
-movies.ipynb: Este Notebook Jupyter se debe correr primero para hacer la transformacion de los datos y generar movies_credits.csv
-movies_recomendacion.ipynb: Este Notebook Jupyter se ejecuta luego de movies.ipynb. Trabaja con movies_credits.csv para poder transformar los datos que             necesitamos para entrenar el modelo de machine learning.
-movies_funciones.ipynb: Este Notebook Jupyter se ejecuta por ultimo. Aca creamos las funciones para adquirir informacion de las peliculas, productoras y            demas, y ademas creamos la funcion de recomendacion para las peliculas, tambien generamos movies_dict.pkl, movies_dataset.pkl, primer_similarity.pkl y              segundo_similarity.pkl
6. images:
-movies_recomendacion.png
-peli2.png
-peli5.png
-peli6.png
7. requirements.txt: Este archivo guarda las librerias del proyecto.


## Sobre la API

Aplicación montada en Streamlit: https://recommendationsystem-pablozmr.streamlit.app/ 

Funciones en la APP:

    Recomendacion de peliculas: Se elije una pelicula y luego se debe hacer click en el boton Recomendar 
    para que la app devuelva 5 peliculas similares con sus respectivos posters

    Buscar peliculas por idioma: Se elije un idioma y luego se debe hacer click en el boton Buscar para 
    que la app devuelva un listado con peliculas que se hayan realizado en ese idioma seleccionado

    Ver duracion y año de la pelicula: Se elije una pelicula y luego se debe hacer click en el boton Ver 
    para que la app devuelva una tabla con la duracion y el año de estreno de la pelicula seleccionada

    Ver informacion de la coleccion de la pelicula: Se elije una coleccion y luego se debe hacer click en 
    el boton Ver info para que la app devuelva cuantas peliculas contiene, cual es la ganancia total de la 
    coleccion, y el promedio de ganancia por pelicula
    
    Ver los paises donde se produjeron las peliculas: Se elije un pais y luego se debe hacer click en el 
    boton Ver info del pais para que la app devuelva el pais seleccionado y la cantidad de peliculas que 
    se realizaron en dicho pais
    
    Ver informacion del exito de las productoras: Se elije una productora y luego se debe hacer click en 
    el boton Ver info de la productora para que la app devuelva el nombre de dicha productora, sus ingresos 
    y la cantidad de peliculas realizadas
    
    Ver informacion de los directores: Se elije un director y luego se debe hacer click en el boton Ver info 
    de los directores para que la app devuelva una tabla con el nombre del director, el retorno total, las 
    peliculas realizadas, el año de estreno, etc.


## Contacto

pabloszmr@gmail.com

www.linkedin.com/in/pablozmr/


