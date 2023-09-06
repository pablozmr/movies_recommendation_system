import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
from streamlit_folium import st_folium
from PIL import Image 
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=175e23e0458bfd5bb9bce2ee18ded653&&laguage=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w780/"+data['poster_path']

def recommend(movie):
    peli_index = movies[movies['title'] == movie].index[0]
    distancia = similarity[peli_index]
    peli_lista = sorted(list(enumerate(distancia)), reverse=True, key= lambda x:x[1])[1:6]
    lista_recomendar = []
    posters_pelis = []
    
    for i in peli_lista:
        movie_id = movies.iloc[i[0]].id
        
        lista_recomendar.append(movies.iloc[i[0]].title)
        posters_pelis.append(fetch_poster(movie_id))
    return lista_recomendar, posters_pelis

def peliculas_idioma(idioma):
    lista_peli = []
    for peli, lang in zip(movies['title'], movies['original_language']):
        if idioma == lang:
            lista_peli.append(peli)
    return lista_peli

def obtener_duracion_y_anio(nombre):
    duracion = movies[movies['title'] == nombre]['runtime'].values[0]
    anio = movies[movies['title'] == nombre]['release_year'].values[0]
    return pd.DataFrame({'Duracion':[str(duracion)], 'Año de estreno':[str(anio)]})

def obtener_informacion_coleccion(name_collection):
    # Filtrar las películas que pertenecen a la colección específica
    peliculas_coleccion = movies[movies['name_collection'] == name_collection]
    
    # Obtener la cantidad de películas
    cantidad_peliculas = len(peliculas_coleccion)
    
    # Calcular las ganancias totales y su promedio
    ganancias_totales = peliculas_coleccion['revenue'].sum()
    promedio_ganancias = peliculas_coleccion['revenue'].mean()
    
    # Devolver los resultados
    return pd.DataFrame({'Cantidad de peliculas':[str(cantidad_peliculas)], 'Ganancias totales': [str(ganancias_totales)], 'Ganancia promedio': [str(promedio_ganancias)]})

def peliculas_pais(pais: str):
    # Filtrar las películas producidas en el país especificado
    peliculas_producidas = movies[movies['production_countries'].str.contains(pais)]
    
    # Obtener la cantidad de películas producidas
    cantidad_peliculas = str(len(peliculas_producidas))
    
    # Devolver el resultado
    # Devolver el resultado
    return pd.DataFrame({'pais': [str(pais)], 'cantidad de peliculas realizadas': [str(cantidad_peliculas)]})

def productoras_exitosas(productora:str):
    # Filtrar las películas realizadas por la productora especificada
    peliculas_productora = movies[movies['production_companies'].str.contains(productora)]
    
    # Obtener la cantidad de películas realizadas por la productora
    cantidad_peliculas = len(peliculas_productora)
    
    # Obtener el total de ingresos de las películas realizadas por la productora
    revenue_total = peliculas_productora['revenue'].sum()
    
    # Devolver el resultado
    return pd.DataFrame({'productora':[productora], 'ingreso_total': [revenue_total],'cantidad':[cantidad_peliculas]})

def get_director(nombre_director):
    # Filtrar el dataset para obtener las películas del director dado
    director_movies = movies[movies['Director'] == nombre_director]

    # Extraer las columnas relevantes del dataset filtrado
    movies_info = director_movies[['title', 'release_date', 'return', 'budget', 'revenue']]

    # Crear una lista de diccionarios con la información de cada película
    movies_list = director_movies['title']

    # Calcular el retorno total del director
    retorno_total_director = director_movies['return'].sum().astype(str)

    # Obtener los años de las películas del director
    anios_peliculas = director_movies['release_year'].astype(str)

    # Calcular el retorno promedio de cada película
    retorno_pelicula = director_movies['return'].astype(str)

    # Obtener los presupuestos y los ingresos de las películas
    budget_pelicula = director_movies['budget'].astype(str)
    revenue_pelicula = director_movies['revenue'].astype(str)

    # Crear el diccionario de respuesta
    return {
        'director': nombre_director,
        'retorno_total_director': retorno_total_director,
        'peliculas': movies_list,
        'anio': anios_peliculas,
        'retorno_pelicula': retorno_pelicula,
        'budget_pelicula': budget_pelicula,
        'revenue_pelicula': revenue_pelicula
    }
    
    
    

movies_dict = pickle.load(open('C:/Users/pablo/OneDrive/Escritorio/Henry/Labs/Dataset/dataset/data/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
primer_similarity = pickle.load(open('C:/Users/pablo/OneDrive/Escritorio/Henry/Labs/Dataset/dataset/data/primer_similarity.pkl', 'rb'))
segundo_similarity = pickle.load(open('C:/Users/pablo/OneDrive/Escritorio/Henry/Labs/Dataset/dataset/data/segundo_similarity.pkl', 'rb'))
similarity = np.concatenate((primer_similarity, segundo_similarity), axis=0)

######################################## Configuración #################################
st.set_page_config(
    page_title = 'Sistema de recomendacion de peliculas',
    page_icon = '🎬',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

######################################### Cabecera ######################################
col1, col2, col3 = st.columns(3)
with col1:
    imghead = Image.open('C:/Users/pablo/OneDrive/Escritorio/Henry/Labs/Dataset/Dataset/images/peli2.png')
    st.image(imghead)
    
with col2:
    imghead = Image.open('C:/Users/pablo/OneDrive/Escritorio/Henry/Labs/Dataset/Dataset/images/peli6.png')
    st.image(imghead)

    
with col3:
    imghead = Image.open('C:/Users/pablo/OneDrive/Escritorio/Henry/Labs/Dataset/Dataset/images/peli5.png')
    st.image(imghead)

st.markdown("<h1 style='text-align: center;'>Sistema de recomendacion de peliculas</h1>", unsafe_allow_html=True)
st.markdown('---')



option = st.selectbox(
    'Cual pelicula viste?',
movies['title'].values
)

if st.button('Recomendar'):
    
    st.write('Podría interesarte...')
    nombres, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(nombres[0])
        st.image(posters[0])

    with col2:
        st.text(nombres[1])
        st.image(posters[1])

    with col3:
        st.text(nombres[2])
        st.image(posters[2])
        
    with col4:
        st.text(nombres[3])
        st.image(posters[3])

    with col5:
        st.text(nombres[4])
        st.image(posters[4])


idioma = st.selectbox('',pd.DataFrame(movies.original_language.unique()))
if st.button('Buscar peliculas por idioma'):
    st.write(pd.DataFrame(peliculas_idioma(idioma)))
    
duracion_anio = st.selectbox('Ver duracion y año de la pelicula', pd.DataFrame(movies.title))
if st.button('Ver'):
    st.write(obtener_duracion_y_anio(duracion_anio))
    
info_coleccion = st.selectbox('Ver informacion de la coleccion de la pelicula', pd.DataFrame(movies.name_collection.unique()))
if st.button('Ver info'):
    st.write(obtener_informacion_coleccion(info_coleccion))
    
pais_produccion = st.selectbox('Ver los paises donde se produjeron las peliculas', movies.production_countries.unique())
if st.button('Ver info del pais'):
    st.write(peliculas_pais(pais_produccion))

    
productora = st.selectbox('Ver informacion del exito de las productoras', movies.production_companies.unique())
if st.button('Ver info de la productora'):
    st.write(productoras_exitosas(productora))
    
director = st.selectbox('Ver informacion de los directores', movies.Director.unique())
if st.button('Ver info de los directores'):
    st.write(pd.DataFrame(get_director(director)))
