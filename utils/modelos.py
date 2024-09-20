
from pydantic import BaseModel, validator, Field
from utils.carga_data import cargar_data1, cargar_data2, cargar_data3, cargar_data4

# Cargar datasets una vez, para reutilizarlos en las validaciones o en las funciones que los necesiten
data_mes_dia = cargar_data1()
data_votos = cargar_data3()
data_creditos = cargar_data2()
data_machine=cargar_data4()

class DiaModel(BaseModel):
    dia: str

    @validator('dia')
    def dia_valido(cls, value):
        dias_validos = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        dia_lower = value.lower()
        if dia_lower not in dias_validos:
            raise ValueError(f"Día inválido: '{value}'. Debe ser uno de {', '.join(dias_validos)}.")
        return dia_lower

class MesModel(BaseModel):
    mes: str

    @validator('mes')
    def mes_valido(cls, value):
        meses_validos = [
            'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
            'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
        ]
        mes_lower = value.lower()
        if mes_lower not in meses_validos:
            raise ValueError(f"Mes inválido: '{value}'. Debe ser uno de {', '.join(meses_validos)}.")
        return mes_lower  # Devolvemos el valor en minúsculas


class ScoreModel(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)

    @validator('titulo')
    def titulo_no_vacio(cls, value):
        if not value.strip():
            raise ValueError("El título no puede estar vacío.")
        return value.strip().lower()


class VotosModel(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)

    @validator('titulo')
    def titulo_no_vacio(cls, value):
        if not value.strip():
            raise ValueError("El título no puede estar vacío.")
        return value


class ActorModel(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=255)

    @validator('nombre')
    def nombre_no_vacio(cls, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return value


class DirectorModel(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=255)

    @validator('nombre')
    def nombre_no_vacio(cls, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return value

    


    