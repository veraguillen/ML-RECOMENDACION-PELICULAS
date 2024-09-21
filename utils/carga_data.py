import pandas as pd
import os



def cargar_data1():
    ruta = os.path.join("datos parquet", "datadia_mes_df1.parquet")
    

    if os.path.exists(ruta):
        try:
            data_mes_dia = pd.read_parquet(ruta)
            return data_mes_dia
        except Exception as e:
            print(f"Error al cargar {ruta}: {e}")
            return None
    else:
        print(f"El archivo {ruta} no existe.")
        return None



def cargar_data2():
    ruta = os.path.join("datos parquet", "data_creditos_df3.parquet")
    if os.path.exists(ruta):
        try:
            data_creditos = pd.read_parquet(ruta)
            return data_creditos
        except Exception as e:
            print(f"Error al cargar {ruta}: {e}")
            return None
    else:
        print(f"El archivo {ruta} no existe.")
        return None


def cargar_data3():
    ruta = os.path.join("datos parquet", "data_votos_df2.parquet")
    if os.path.exists(ruta):
        try:
            data_votos = pd.read_parquet(ruta)
            return data_votos
        except Exception as e:
            print(f"Error al cargar {ruta}: {e}")
            return None
    else:
        print(f"El archivo {ruta} no existe.")
        return None


def cargar_data4():
    ruta = os.path.join("datos parquet", "data_machine_df4.parquet")
  
    if os.path.exists(ruta):
        try:
            data_machine = pd.read_parquet(ruta)
            return data_machine
        except Exception as e:
            print(f"Error al cargar {ruta}: {e}")
            return None
    else:
        print(f"El archivo {ruta} no existe.")
        return None


