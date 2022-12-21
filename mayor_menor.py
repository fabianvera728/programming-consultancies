# funcion para calcular la posicion del mayor elemento de una lista
def mayor_lista(lista):
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor


def menor_lista(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor


def posicion_mayor(lista):
    mayor = lista[0]
    posicion = 0
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            posicion = i
    return posicion


def posicion_menor(lista):
    menor = lista[0]
    posicion = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicion = i
    return posicion


# funcion para retornar un numero invertido
def invertir(numero):
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero = numero // 10
    return invertido


# data una lista de numero calcular el espejo de la lista
# ejemplo
# [564, 432, 123] -> [465, 234, 321]
def espejo(lista):
    lista_espejo = []
    for i in range(len(lista)):
        lista_espejo.append(lista[len(lista) - 1 - i])
    return lista_espejo
