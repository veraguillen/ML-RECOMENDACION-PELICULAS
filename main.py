from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
# Importar funciones y modelos necesarios
from utils.funciones import cantidad_filmaciones_dia, cantidad_filmaciones_mes, score_titulo, votos_titulo, get_actor, get_director, get_recommendations
from utils.carga_data import cargar_data1, cargar_data2, cargar_data3, cargar_data4
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
            

# Cargar los datasets
data_mes_dia = cargar_data1()
data_votos = cargar_data3()
data_creditos = cargar_data2()
data_machine = cargar_data4()

# Endpoint para consultar la cantidad de películas por día de la semana
@app.get("/cantidad_filmaciones_dia/")
def obtener_cantidad_filmaciones_dia(dia: str = Query(..., description="Día de la semana en minúsculas")):
    dia = dia.lower().strip()
    
    # Validar que el día proporcionado es válido
    dias_validos = data_mes_dia['dia_tex'].str.lower().unique()
    if dia not in dias_validos:
        raise HTTPException(status_code=400, detail=f"El día '{dia}' no es válido. Por favor, introduce un día válido.")
    
    # Llamar a la función para obtener la cantidad de películas
    try:
        resultado = cantidad_filmaciones_dia(data_mes_dia, dia)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"resultado": resultado}

# Endpoint para consultar la cantidad de películas por mes
@app.get("/cantidad_filmaciones_mes/")
def obtener_cantidad_filmaciones_mes(mes: str = Query(..., description="Mes en minúsculas")):
    mes = mes.lower().strip()
    
    # Validar que el mes proporcionado es válido
    meses_validos = data_mes_dia['mes_tex'].str.lower().unique()
    if mes not in meses_validos:
        raise HTTPException(status_code=400, detail=f"El mes '{mes}' no es válido. Por favor, introduce un mes válido.")
    
    # Llamar a la función para obtener la cantidad de películas
    try:
        resultado = cantidad_filmaciones_mes(data_mes_dia, mes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"resultado": resultado}

# Endpoint para obtener el score y el año de estreno de una película por su título
@app.get("/score_titulo/")
def obtener_score_titulo(titulo: str = Query(..., description="Título de la película")):
    titulo = titulo.lower().strip()
    
    # Verificar si el título es válido
    if not titulo:
        raise HTTPException(status_code=400, detail="El título proporcionado no es válido. Por favor, introduce un título correcto.")
    
    # Llamar a la función para obtener la información de la película
    try:
        resultado = score_titulo(data_votos, titulo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if "No se encontró ninguna película" in resultado:
        raise HTTPException(status_code=404, detail=resultado)
    
    return {"resultado": resultado}

# Endpoint para obtener la cantidad de votos y el promedio de votos de una película
@app.get("/votos_titulo/")
def obtener_votos_titulo(titulo: str = Query(..., description="Título de la película")):
    titulo = titulo.lower().strip()
    
    # Verificar si el título es válido
    if not titulo:
        raise HTTPException(status_code=400, detail="El título proporcionado no es válido. Por favor, introduce un título correcto.")
    
    # Llamar a la función para obtener la información de la película
    try:
        resultado = votos_titulo(data_votos, titulo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if "No se encontró ninguna película" in resultado:
        raise HTTPException(status_code=404, detail=resultado)
    
    return {"resultado": resultado}

# Endpoint para obtener información sobre un actor
@app.get("/get_actor/")
def get_actor_endpoint(nombre_actor: str):
    resultado = get_actor(data_creditos, nombre_actor)

    if "No se encontró información" in resultado:
        raise HTTPException(status_code=404, detail=resultado)
    
    return {"mensaje": resultado}

# Endpoint para obtener información sobre un director
@app.get("/get_director/")
def obtener_director(nombre: str = Query(..., description="Nombre del director")):
    nombre_director = nombre.lower().strip()
    
    # Verificar si el nombre es válido
    if not nombre_director:
        raise HTTPException(status_code=400, detail="El nombre proporcionado no es válido. Por favor, introduce un nombre correcto.")
    
    # Llamar a la función para obtener la información del director
    try:
        resultado = get_director(data_creditos, nombre_director)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if "No se encontró ninguna película" in resultado:
        raise HTTPException(status_code=404, detail=resultado)
    
    return {"resultado": resultado}

# Modelo de entrada de la solicitud para recomendaciones
class RecommendationRequest(BaseModel):
    title: str

# Endpoint para obtener recomendaciones
@app.get("/recommendations/")
def recommend_movies(title: str):
    recommendations = get_recommendations(title, data_machine)
    return {"recommendations": recommendations.tolist()}

# Iniciar la aplicación en el puerto 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)