#usted ha recibido un nuevo robot de regalo de cumpleaños, el robot tiene una brujula
#interna que le permite saber hacia donde esta mirando actualmente(punto cardinal),
#el robot tiene un control remoto que permite girarlo de acuerdo a los siguientes comandos
#usted debe escribir una funcion que dados 3 comandos que se envien calcule
#la orientacion final del robot
#representacion de los puntos cardinales
#N=norte
#S=sur
#E=este
#W=oeste

#comandos:
#L=giro a la izquierda
#R=giro a la derecha
#H=media vuelta
# . mantenga posicion

#nombre de la funcion: movimiento_robot
#parametros: posicion_actual:str
#            giro1:str
#            giro2:str
#            giro3:str(        )

def giro_norte(giro):
    if giro == "L":
        posicion_final = "W"
    elif giro == "R":
        posicion_final = "E"
    elif giro == "H":
        posicion_final = "N"
    elif giro == ".":
        posicion_final = "N"
    return posicion_final

def giro_sur(giro):
    if giro == "L":
        posicion_final = "E"
    elif giro == "R":
        posicion_final = "W"
    elif giro == "H":
        posicion_final = "S"
    elif giro == ".":
        posicion_final = "S"
    return posicion_final

def giro_este(giro):
    if giro == "L":
        posicion_final = "N"
    elif giro == "R":
        posicion_final = "S"
    elif giro == "H":
        posicion_final = "E"
    elif giro == ".":
        posicion_final = "E"
    return posicion_final
def giro_oeste(giro):
    if giro == "L":
        posicion_final = "S"
    elif giro == "R":
       posicion_final = "N"
    elif giro == "H":
        posicion_final = "W"
    elif giro == ".":
        posicion_final = "W"
    return posicion_final

def movimiento_robot(posicion_actual: str, giro: str) -> str:
    if posicion_actual == "N":
        posicion_final = giro_norte(giro)
    if posicion_actual == "S":
        posicion_final = giro_sur(giro)
    if posicion_actual == "E":
        posicion_final = giro_este(giro)
    if posicion_actual == "W":
        posicion_final = giro_oeste(giro)
    return posicion_final

def movimientos_robot(posicion_inicial: str, giro1: str, giro2:str , giro3:str) -> str:
    posicion_actual:str
    posicion_actual = movimiento_robot(posicion_inicial, giro1)
    posicion_actual = movimiento_robot(posicion_actual, giro2)
    posicion_actual = movimiento_robot(posicion_actual, giro3)
    return posicion_actual

movs = ['L', 'R', 'H', '.']
actual2 = 'N'
for i in movs:
    actual2 = movimiento_robot(actual2, i)

print(movimientos_robot("N", "R", "L", "H"))

