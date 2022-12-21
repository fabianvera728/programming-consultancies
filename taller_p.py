dias = [[1, "lunes", 0, 0], [2, "martes", 0, 0],
        [3, "miercoles", 0, 0], [4, "jueves", []],
        [5, "viernes"]]

pasteles = [[1, "jamon", 12], [2, "jamon y queso", 34], [
    3, "queso", 34], [4, "pollo", 43], [5, "carne", 123]]

pastelesXdia = [[0, 0]] * 5
pastelesDia = []
for i in range(5):
    pastelesDia.append(pastelesXdia)

def elegirPastel() -> int:
    entrada = int(input("Eliga su pastel"))
    numPasteles = int(input("Numero de pasteles"))
    return [entrada, numPasteles]


def mostrarPasteles():
    entrada = ""
    print("Menu elegir pastel \n")
    while True:
        for i in pasteles:
            print(i[0]+" - nombre: "+i[1]+" - precio: " + i[2])
        entrada = elegirPastel()
        if (entrada > 0 and entrada <= 5):
            break
    return entrada


def mostrarDias():
    print("Elegir dia de la semana")
    for i in dias:
        print(i[0]+" - "+i[1])
    return int(input("Escriba el dia de la semana"))


def agregarPastelEnCalendario(dia: int):
    [tipoPastel, numPastelesAComprar] = mostrarPasteles()
    # numeroActualEnElDia = pastelesDia[dia][tipoPastel-1][0]
    pastelesDia[dia-1][tipoPastel-1][0] += numPastelesAComprar
    pastelesDia[dia-1][tipoPastel-1][1] += pasteles[tipoPastel -
                                                    1][3] * numPastelesAComprar


def obtenerMayorLista(lista):
    j = 0
    posMayor = 0
    mayor = lista[j][0]
    for i in lista:
        if i[0] > mayor:
            mayor = i[0]
            posMayor = j
        j += 1
    return posMayor


def calcularMaximoEnUnDia(dia: int) -> int:
    diaPasteles = pastelesDia[dia-1]
    valores = [0, 0, 0, 0, 0]
    contador = 0
    for i in diaPasteles:
        valores[contador] = i[0]
        contador += 1
    posMayor = obtenerMayorLista(valores)
    return posMayor


def compra():
    dia = mostrarDias()
    while True:
        print("1. Comprar pastel")
        agregarPastelEnCalendario(dia)
