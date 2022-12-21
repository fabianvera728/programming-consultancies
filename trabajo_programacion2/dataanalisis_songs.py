# Pruebas con pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Archivo del proyecto
# src: ./songs_normalized.csv

# Ubique las columnas que son de tipo numérico, aplique un filtro para
# obtener un nuevo dataframe y genere un resumen estadístico de los datos
# que a su criterio son más relevantes. Plasme los resultados en el documento
# de Word y haga una breve interpretación de sus valores.

# usar pandas para leer el archivo
df = pd.read_csv('songs_normalize.csv')

# ubicar las columnas que son de tipo numérico
df_numeric = df.select_dtypes(include=['int64', 'float64'])

# aplicar un filtro para obtener un nuevo dataframe
df_numeric_filtered = df_numeric[df_numeric['popularity'] > 80]

# generar un resumen estadístico de los datos que a su criterio son más relevantes
# print(df_numeric_filtered)
df_numeric_filtered.describe()


# plasmar 3 ideas de analisis que tenga para la base de datos de canciones de spotify
# 1. ¿Cual es el promedio de duración de las canciones?
# 2. ¿Cual es el promedio de popularidad de las canciones?
# 3. ¿Cual es el promedio de duración de las canciones que tienen una popularidad
#    mayor a 80?

# 1. ¿Cual es el promedio de duración de las canciones?
print(df_numeric_filtered['duration_ms'].mean())

# 2. ¿Cual es el promedio de popularidad de las canciones?
print(df_numeric_filtered['popularity'].mean())

# 3. ¿Cual es el promedio de duración de las canciones que tienen una popularidad
#    mayor a 80?
print(df_numeric_filtered[df_numeric_filtered['popularity']
      > 80]['duration_ms'].mean())

# agrupar por el año de la canción
df_numeric_filtered_grouped = df_numeric_filtered.groupby('year')
print(df_numeric_filtered_grouped.describe())

# realizar una grafica de barras para los años de las canciones con matplotlib y numpy
df_numeric_filtered_grouped['duration_ms'].mean().plot(kind='bar')


# df_numeric_filtered_grouped['duration_ms'].mean().plot(kind='bar')
df_numeric_filtered_grouped.mean().plot(kind='bar')
