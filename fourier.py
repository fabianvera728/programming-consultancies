## funcion para calcular potencia
import math

def potencia(base,exponente):
    return math.pow(base,exponente)

def a0():
    return math.pi/2

def an(n):
    return (1-potencia((-1),n))/ (potencia(n,2) * math.pi)

def bn(n):
    return 1/n

def coseno(x):
    return math.cos(x)

def seno(x):
    return math.sin(x)

def w0():
    return 1

def sumatoria(intervalos, x):
    indice = 1 
    resultado = 0
    while(indice < intervalos):
        an_cos = an(indice)* coseno(indice*w0()*x)
        bn_sen = bn(indice)* seno(indice*w0()*x)
        resultado += an_cos + bn_sen
        indice += 1
    return resultado

def fx(x):
    intervalos = 10
    resultado = (a0()/2) + sumatoria(intervalos, x)
    return resultado

## codigo prueba
print("Resultado: ", fx(math.pi/2))
print("Resultado: ", fx(-math.pi/2))
print("Resultado: ", fx(math.pi/4))
print("Resultado: ", fx(-math.pi/4))





