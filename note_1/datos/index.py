import pandas as pd
import numpy as np

datos = pd.read_csv('./Iris.csv')
for col in datos.select_dtypes(include='number').columns:
    print(f"Column: {col}")
    media = np.mean(datos[col])
    mediana = np.median(datos[col])
    desviacion_estandar = np.std(datos[col])
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion_estandar}")