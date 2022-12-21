# funcion para calcular el fibonacci n de forma iterativa
def fibonacci_iterativo(n: int) -> int:
    resultado: int = 0
    f0: int = 0
    f1: int = 1
    index = 0
    while index < n:
        aux = f0
        f0 = f1
        f1 = aux + f1
        # resultado = resultado + f0
        # f0 = f1
        # f1 = f0 + f1
        index += 1
    return f0

# codigo de prueba
print(fibonacci_iterativo(10))
