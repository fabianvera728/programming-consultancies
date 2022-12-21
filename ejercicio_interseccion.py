# funcion que calcule la interseccion de dos listas
# lista1 = [1,2,3]
# lista2 = [2,3]
# resultado = [2,3]
def interseccion(lista1, lista2):
    lista3 = []
    while len(lista1) > 0:
        if lista1[0] in lista2:
            lista3.append(lista1[0])
        lista1.pop(0)
    return lista3

# funcion para calcular la inclusion de una lista en otra
# lista1 = [1,2,3]
# lista2 = [1,2,4,3]
def inclusion(lista1, lista2):
    index = 1
    while index < len(lista1):
        if lista1[index] not in lista2:
            return False
        index += 1
    return True


# funcion para saber si un numero es primo
def es_primo(numero):
    if numero == 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, numero, 2):
        if numero % i == 0:
            return False
    return True


# funcion para generar una lista de numeros primos de 1 a n  
def generar_primos(n):
    lista = []
    index = 1
    while index <= n:
        if es_primo(index):
            lista.append(index)
        index += 1
    # for i in range(1, n + 1):
    #     if es_primo(i):
    #         lista.append(i)
    return lista






