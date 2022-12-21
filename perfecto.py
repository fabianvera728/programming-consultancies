# funcion para saber si un numero es perfecto
def es_perfecto(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if suma == num:
        return True
    else:
        return False
