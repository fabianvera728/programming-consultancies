import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_excel():
    """
    Codigo que permite leer un excel
    : params
    12 columnas
    : return
    12 columanas de datos de 235 estudiantes entrevistados
    """
    df = pd.read_csv("Student_Behaviour.csv")
    return df


def get_info(df):
    """
    Codigo que permite extraer la informacion necesaria para saber que tipo de datos posee cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     informació sobre los tipos de datos de cada columna
    """
    return df.info()


def get_numeric_columns(df):
    """
    Codigo que permite extraer las columnas numericas de un dataframe
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
        columnas numericas de un dataframe
    """
    return df._get_numeric_data()


def get_max_values(df):
    """
    Codigo que permite calcular los valores maximos de cada columna numerica
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     valores maximos de cada columna numerica
    """
    auxDf = get_numeric_columns(df)
    return auxDf.max()


def get_min_values(df):
    """
    Codigo que permite calcular los valores minimos de cada columna numerica
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     valores minimos de cada columna numerica
    """
    auxDf = get_numeric_columns(df)
    return auxDf.min()


def get_mean(df):
    """
    Codigo que permite calcular el promedio de los datos de cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     promedio de los datos de cada columna
    """
    auxDf = get_numeric_columns(df)
    return auxDf.mean()


def get_mode(df):
    """
    Codigo que permite calcular el valor que mas se repite en cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     valor que mas se repite en cada columna
    """
    auxDf = get_numeric_columns(df)
    return auxDf.mode()


def graph_max_values(df):
    """
    Codigo que permite graficar los maximos de cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     grafica de los maximos de cada columna
    """
    get_max_values(df).plot(kind='bar').set_title('Maximos')
    plt.show()


def graph_min_values(df):
    """
    Codigo que permite graficar los minimos de cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     grafica de los minimos de cada columna
    """
    get_min_values(df).plot(kind='bar').set_title('Minimos')
    plt.show()


def graph_prom(df):
    """
    Codigo que permite graficar el promedio de cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     grafica del promedio de cada columna
    """
    get_mean(df).plot(kind='bar').set_title('Promedio')
    plt.show()


    """
    Codigo que permite graficar el modo de cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     grafica del modo de cada columna
    """
def graph_mode(df):
    get_mode(df).plot(kind='bar').set_title('Modo')
    plt.show()


def graph_count(df):
    """
    Codigo que permite graficar el conteo de cada valor en cada columna
    : params
     12 columnas, Weight(KG),Height(CM),salary expectation, 10th Mark,12th Mark,college mark, etc
    : return
     grafica del conteo de cada valor en cada columna
    """
    auxDf = get_numeric_columns(df)
    auxDf.hist(bins=10)
    plt.show()


# Area de pruebas
# df = read_excel()
# print("\n ****** \n")
# print("\nMaximos de los datos de cada columna")
# print(get_max_values(read_excel()))
# print(get_min_values(df))
# print("\nMinimos de los datos de cada columna")
# print(get_min_values(df))
# print("\nPromedio de los datos de cada columna")
# get_mean(df)
# print("\nValor que mas se repite en cada columna")
# print(get_mode(df))
# graph_count(df)
# graph_max_values(df)
# graph_min_values(df)
# graph_prom(df)
# graph_mode(df)
