import numpy as np
import math as ma

# series de taylor para calcular el seno y coseno utilizando cooperacion de funciones.

def factorial(n):
    rtaftl=1
    if(n>0):
        i=1
        while(i<=n):
            rtaftl=rtaftl*i
            i=i+1
    return(rtaftl)
#factorial(n)
#funcion que calcula el factorial de un numero, sabiendo que el factorial de (0) es uno (1)
#parametros:
    #n: numero entero positivo al que se le va a calcular el factorial
#retorno:
    #numero entero positivo con el calculo del factorial
#casos de prueba
    #factorial(0) --> 1
    #factorial(5) --> 120

def potencia(base,exponente):
    rtapotencia=1
    if(exponente>=0):
        i=0
        while(i<exponente):
            rtapotencia=rtapotencia*base
            i=i+1
    return(rtapotencia)
#potencia(base,exponente)
#funcion que calcula la potencia de un numero dado su base y exponente
#parametros:
    #base: numero entero positivo que corresponde a la base
    #exponente: numero entero positivo que corresponde al exponente
#retorno:
    #rtapotencia: numero entero positivo que corresponde al calculo de la potencia
#casos de prueba
    #potencia(2,5)--> 32
    #potencia(2,0)--> 1
    #potencia(0,2)--> 0

def calculosenoradianes(anguloradianes,n):
    rta=0
    if(n>0):
        k=0
        while(k<=n):
            rta=rta+(potencia(-1,k) * potencia(anguloradianes,(2*k+1)) / factorial(2*k+1))
            k=k+1
    return(rta)
#funcion que calcula el seno de un angulo en radianes utilizando la serie de taylor, n es el numero de veces que se aplica la sumatoria
#parametros:
    #anguloradianes: valor real que corresponde al angulo en radianes al que se le va a calcular el seno
    #n: valor entero positivo que determina el numero de sumas sucesivas de la serie
#retorno
    #rta: valor real del seno del angulo

def calculocosenoradianes(anguloradianes,n):
    rta=0
    if(n>0):
        k=0
        while(k<=n):
            rta=rta+(potencia(-1,k)*potencia(anguloradianes,(2*k))/factorial(2*k))
            k=k+1
    return(rta)

#calculocosenoradianes()
#funcion que calcula el coseno de un angulo en radianes, utilizando la serie de taylor
#parametros:
    #anguloradianes: valor real que corresponde al angulo en radianes al que se le va a calcular el coseno
    #n:valor entero positivo que determina el numero de sumas sucesivas de la serie
#retorno:
    #rta:valor real del coseno del angulo dado


#fx()
#autores: Eric Orozco Suarez(1006845874), Jesus David Rangel Zambrano(1004505154),Arnold Ruben Robayo Camargo(1007369297)
#funcion que calcula la serie de fourier de una funcion periodica f(x) de periodo T (señal)
    #k:valor entero positivo que determina el numero de sumas sucesivas de la serie
#retorno:
    #rta: la aproximacion de f(x) mediante sumas parciales de la serie de fourier

def fx(k):
    pi=3.14159
    ao=(pi/2)/2
    intervalo_seno = 1000
    n=1
    while(n<=k):
        rta=(1-(potencia(-1,n))/(potencia(n,2)*pi))*(calculocosenoradianes((n*1),intervalo_seno)+((1/n)*calculosenoradianes((n*1),intervalo_seno)))
        n=n+1
    return (rta)

#casos de prueba fx
c=8
print(f'Aproximación de f(x) mediante {c} sumas parciales de la serie: \n{fx(c)}\n')
b = 6
print(f'Aproximación de f(x) mediante {b} sumas parciales de la serie: \n{fx(b)}\n')
a = 10
print(f'Aproximación de f(x) mediante {a} sumas parciales de la serie: \n{fx(a)}\n')

##CASOS DE PRUEBA COSENO
x = 45
print(f'Calcular Coseno de {x} grados en radianes: \n{calculocosenoradianes(x,15)}\n')
y = 90
print(f'Calcular Coseno de {y} grados en radianes: \n{calculocosenoradianes(y,15)}\n')
z = 180
print(f'Calcular Coseno de {z} grados en radianes: \n{calculocosenoradianes(z,15)}\n')

##CASOS DE PRUEBA SENO
o = 45
print(f'Calcular Seno de {o} grados en radianes: \n{calculosenoradianes(o,15)}\n')
p = 90
print(f'Calcular Seno de {p} grados en radianes: \n{calculosenoradianes(p,15)}\n')
q = 180
print(f'Calcular Seno de {q} grados en radianes: \n{calculosenoradianes(q,15)}\n')

##CASOS DE PRUEBA POTENCIA
a = 2
b = 5
c = 6
d = 7
print(f'Calcular la potencia de 2 potencia {b} \n{potencia(2,5)}\n')
print(f'Calcular la potencia de 2 potencia {c} \n{potencia(2,6)}\n')
print(f'Calcular la potencia de 2 potencia {d} \n{potencia(2,7)}\n')

##CASOS DE PRUEBA FACTORIAL

h = 2
i = 5
j = 6
print(f'Calcular El factorial de {h} \n{factorial(h)}\n')
print(f'Calcular El factorial de {i} \n{factorial(i)}\n')
print(f'Calcular El factorial de {j} \n{factorial(j)}\n')







