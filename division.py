# funcion para calcular la division de a entre b usando restas sucesivas usando while
def divisor_while(a,b):
    if b == 0:
        return 0
    else:
        c = 0
        while a >= b:
            a = a - b
            c = c + 1
        return c

# funcion para calcular el residuo de a entre b usando restas sucesivas usando while
def division_modular(a,b):
    residuo = a - divisor_while(a,b)*b
    return residuo

# codigo de prueba
print(divisor_while(10,3))
print(division_modular(10,3))
