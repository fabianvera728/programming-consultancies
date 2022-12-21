# dado un numero natural n cree una funcion que calcule cuantos numeros primos hay hasta el 
# numero n 
def es_primo(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True








def primos(n):
    contador = 0
    for i in range(1,n+1):
        if es_primo(i):
            contador += 1
    return contador
