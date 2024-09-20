import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.carga_data import cargar_data1, cargar_data2, cargar_data3, cargar_data4
import numpy as np

# Cargar los datasets
data_mes_dia = cargar_data1()
data_votos = cargar_data3()
data_creditos = cargar_data2()
data_machine = cargar_data4()

# Cargar el dataset y el modelo entrenado
#cosine_sim = cargar_data_machine5()

def cantidad_filmaciones_dia(data_mes_dia, dia):
    dia = dia.lower().strip()
    dias_validos = data_mes_dia['dia_tex'].str.lower().unique()

    if dia not in dias_validos:
        return f"El día '{dia}' no es válido. Por favor, introduce un día válido."
    
    peliculas_dia = data_mes_dia[data_mes_dia['dia_tex'].str.lower() == dia]
    cantidad = len(peliculas_dia)
    
    return f"La cantidad de películas estrenadas en los días {dia.capitalize()} es de: {cantidad}"

def cantidad_filmaciones_mes(data_mes_dia, mes):
    mes = mes.lower().strip()
    meses_validos = data_mes_dia['mes_tex'].str.lower().unique()

    if mes not in meses_validos:
        return f"El mes '{mes}' no es válido. Por favor, introduce un mes válido."
    
    peliculas_mes = data_mes_dia[data_mes_dia['mes_tex'].str.lower() == mes]
    cantidad = len(peliculas_mes)
    
    return f"La cantidad de películas estrenadas en el mes de {mes.capitalize()} es de: {cantidad}"

def score_titulo(data_votos, titulo_de_la_filmación):
    titulo_de_la_filmación = titulo_de_la_filmación.lower().strip()

    if not titulo_de_la_filmación:
        return "El título proporcionado no es válido. Por favor, introduce un título correcto."
    
    pelicula = data_votos[data_votos['title'].str.lower() == titulo_de_la_filmación]

    if not pelicula.empty:
        titulo = pelicula.iloc[0]['title']
        año = pelicula.iloc[0].get('año', 'Desconocido')  # Verifica si 'año' está presente
        score = pelicula.iloc[0]['vote_average']
        
        return f"La película '{titulo}' fue estrenada en el año {año}, con un score de {score}."
    else:
        return "No se encontró ninguna película con ese título."

def votos_titulo(data_votos, titulo_de_la_filmación):
    titulo_de_la_filmación = titulo_de_la_filmación.lower().strip()

    if not titulo_de_la_filmación:
        return "El título proporcionado no es válido. Por favor, introduce un título correcto."
    
    pelicula = data_votos[data_votos['title'].str.lower() == titulo_de_la_filmación]

    if not pelicula.empty:
        titulo = pelicula.iloc[0]['title']
        cantidad_votos = pelicula.iloc[0]['vote_count']
        promedio_votos = pelicula.iloc[0]['vote_average']
        año_estreno = pelicula.iloc[0].get('año', 'Desconocido')  # Verifica si 'año' está presente
        
        if cantidad_votos >= 2000:
            return (f"La película '{titulo}' fue estrenada en el año {año_estreno}. "
                    f"La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}.")
        else:
            return "La película no cumple con el requisito de tener al menos 2000 valoraciones."
    else:
        return "No se encontró ninguna película con ese título."

def get_actor(data_creditos, nombre_actor: str) -> str:
    # Normalizar el nombre del actor
    nombre_actor = nombre_actor.lower().strip()

    if not nombre_actor:
        return "El nombre proporcionado no es válido. Por favor, introduce un nombre correcto."

    # Verificar si las columnas contienen listas o cadenas separadas por comas
    if isinstance(data_creditos['female_actors'].iloc[0], str):
        # Si es una cadena, dividirla en listas
        data_creditos['female_actors'] = data_creditos['female_actors'].apply(lambda x: x.split(","))
    if isinstance(data_creditos['male_actors'].iloc[0], str):
        # Si es una cadena, dividirla en listas
        data_creditos['male_actors'] = data_creditos['male_actors'].apply(lambda x: x.split(","))

    # Filtrar las películas en las que ha participado el actor (en las columnas 'female_actors' y 'male_actors')
    data_filtered = data_creditos[
        data_creditos['female_actors'].apply(lambda x: nombre_actor in [actor.lower().strip() for actor in x]) |
        data_creditos['male_actors'].apply(lambda x: nombre_actor in [actor.lower().strip() for actor in x])
    ]

    if not data_filtered.empty:
        cantidad_peliculas = len(data_filtered)
        retorno_total = data_filtered['revenue'].sum(skipna=True)
        promedio_retorno = data_filtered['revenue'].mean(skipna=True)

        return (f"El actor/actriz {nombre_actor.capitalize()} ha participado en {cantidad_peliculas} filmaciones. "
                f"El mismo ha conseguido un retorno total de {retorno_total} dólares, con un promedio de {promedio_retorno} dólares por filmación.")
    else:
        return f"No se encontró información de películas con el actor '{nombre_actor.capitalize()}'."

def get_director(data_creditos, nombre_director):
    nombre_director = nombre_director.lower().strip()

    if not nombre_director:
        return "El nombre proporcionado no es válido. Por favor, introduce un nombre correcto."
    
    data_filtered = data_creditos[data_creditos['director_name'].str.lower().str.strip() == nombre_director]

    if not data_filtered.empty:
        retorno_total = data_filtered['revenue'].sum(skipna=True)
        roi_mean = data_filtered['roi'].mean(skipna=True)
        
        detalles_peliculas = "\n".join(
            [
                f"FILM: '{row['title']}', ESTRENO: {row['release_date']}, "
                f"RETORNO DE INVERSIÓN: {row['revenue']} dólares, COSTO/PRESUPUESTO: {row['budget']} dólares, "
                f"GANANCIA de: {row['revenue'] - row['budget']} dólares."
                for _, row in data_filtered.iterrows()
            ]
        )
        
        return (f"{nombre_director.capitalize()} como DIRECTOR ha tenido un RETORNO TOTAL DE: {retorno_total} dólares y un ROI promedio de: {roi_mean:.2f}.\n\n"
                f"Detalles de las películas:\n{detalles_peliculas}")
    else:
        return "No se encontró ninguna película con ese director."
    




def get_index_from_title(title, data_machine):
    title = title.lower().strip()
    return data_machine[data_machine['title'].str.lower() == title].index[0]

def get_recommendations(title, data_machine):
    try:
        # Vectorizar los datos usando TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(data_machine['combined_processed'])
        
        # Obtener el índice de la película buscada
        idx = get_index_from_title(title, data_machine)
        
        # Calcular la similitud del coseno
        cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)
        
        # Enumerar las películas y ordenarlas por similitud
        sim_scores = list(enumerate(cosine_sim[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Obtener los índices de las 5 películas más similares
        movie_indices = [i[0] for i in sim_scores[1:6]]
        
        # Devolver los títulos de las películas recomendadas
        return data_machine['title'].iloc[movie_indices]
    
    except IndexError:
        return ["No se encontró la película en los datos"]

