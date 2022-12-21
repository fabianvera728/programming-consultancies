import random

# funcion para ver si un elemento esta en una lista 
def esta_elemento_en_lista(lista: list, elemento: float) -> bool:
    for i in lista:
        if i == elemento:
            return True
    return False

def esta_elemento_en_lista(lista: list, elemento: float) -> bool:
    esta_en_lista: bool = False
    indice: int = 0
    while indice < len(lista):
        if lista[indice] == elemento:
            esta_en_lista = True
            break
        indice += 1
    return esta_en_lista

# Funcion que genere una lista de numeros aleatorios
# sin que se repitan en un rango
def generar_lista_aleatorios_sin_repetir_en_un_rango(tamano: int,
                                               minimo: float,
                                               maximo: float) -> list:
    lista: list = []
    while len(lista) < tamano:
        numero: float = round(random.random() * (maximo - minimo) + minimo, 2)
        if not esta_elemento_en_lista(lista, numero):
            lista.append(numero)
    return lista



# generar codigo de prueba para la Funcion
print(generar_lista_aleatorios_sin_repetir_en_un_rango(12, 1, 10))


