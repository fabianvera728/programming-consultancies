# HACER FUNCIONES PARA REALIZAR OPERACIONES
# ENTRE CONJUNTOS DADAS DOS LISTAS, PRIMERO
# A INTERCEPTADO B, elementos de a que estan en b
def a_interceptado_b(a, b):
    resultado = []
    for i in a:
        if i in b:
            resultado.append(i)
    return resultado

# SEGUNDA A UNIDO B, TERCERO
# A DIFERENTE DE B, CUARTA A DIFERENCIA
def a_diferente_b(a, b):
    resultado = []
    for i in a:
        if i not in b:
            resultado.append(i)
    return resultado

# SIMETRICA DE B
def simetrica_b(a, b):
    resultado = []
    for i in a:
        if i not in b:
            resultado.append(i)
    for i in b:
        if i not in a:
            resultado.append(i)
    return resultado
