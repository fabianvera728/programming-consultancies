"""
Una compañía de transportes que tiene sucursales en 20 ciudades del país, quiere
saber la distancia que recorre un conductor al ir de una ciudad a otra. Los datos referentes a las
distancias están indicados como se muestra a continuación:
0 dist0,1 dist0,2 . . . dist0,19
Dist1,0 0 dist1,2 . . . dist1,19
Dist2,0 dist2,1 0 . . . dist2,19
… … … . . . …
Dist19,0 dist19,1 dist19,2 . . . 0
Dónde:
Dist (i, j) > 0representa que hay carretera de la ciudad i a la ciudad j y la distancia existente
entre ambas ciudades.
Dist (i, j) = 0si i diferente a j, representa que no hay carretera entre la ciudad i y la ciudad j.
Elabore las funciones necesarias que permitan dada una matriz como la descrita, calcular la
distancia que debe recorrer un conductor ir de la ciudad “a” a la ciudad “b”. Si no existe
carretera directa, entonces deberá encontrar una ciudad intermedia “c”, para hacer el recorrido
de la ciudad “a” a la ciudad “c“ y de la ciudad “c” a la cuidad “b”.
"""


def calcular_distancia(matriz, a, b):
    """
    Calcula la distancia entre dos ciudades
    """
    if a == b:
        return 0
    else:
        distancia = 0
        matriz_aux = matriz[a]
        if matriz_aux[b] != 0:
            distancia = matriz_aux[b]
            return distancia
        else:
            for i in range(len(matriz)):
                if matriz[a][i] != 0 and matriz[i][b] != 0:
                    distancia = matriz[a][i] + matriz[i][b]
                    return distancia
            return "No existe camino a esa ciudad"


# area de prueba

matriz_distancias = [
    [0, 12, 10, 15, 20, 25, 30, 35, 40, 45, 50,
        55, 60, 65, 70, 75, 80, 85, 90, 0],
    [5, 0, 15, 20, 25, 30, 35, 40, 45, 50, 55,
        60, 65, 70, 75, 80, 85, 90, 95, 100],
    [10, 15, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    [15, 20, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    [20, 25, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    [25, 30, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    [30, 35, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    [35, 40, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    [40, 45, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    [45, 50, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    [50, 55, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
    [55, 60, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40],
    [60, 65, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35],
    [65, 70, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30],
    [70, 75, 60, 0, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25],
    [75, 80, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20],
    [80, 85, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15],
    [85, 90, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10],
    [90, 95, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5],
    [95, 0, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
]

print("Distancia entre la ciudad 3 y la 14 ")
print(calcular_distancia(matriz_distancias, 3, 14))
print("\nDistancia entre la ciudad 0 y la 19 ")
print(calcular_distancia(matriz_distancias, 0, 19))
print("\nDistancia entre la ciudad 0 y la 18 ")
print(calcular_distancia(matriz_distancias, 0, 18))
