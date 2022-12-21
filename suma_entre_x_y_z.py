# dados dos numeros X y Z, donde X es menor que Z, hacer una funcion para calcular
# la suma de los numeros entre X y Z 
def suma(x,z):
    if x < z:
        suma = 0
        for i in range(x,z+1):
            suma += i
        return suma
    else:
        return "Error valores incorrectos"
