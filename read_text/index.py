# -- coding:utf-8 --

"""
@author: Fabian Hernando Vera Carrillo
"""


def traer_de_archivo(nombre_archivo: str) -> list:
    rta = []
    archivo = open(nombre_archivo, 'r')
    for linea in archivo:
        rta.append(eval(linea))

    archivo.close
    return(rta)


def estudiante_como_cadena(e: dict) -> str:
    cadena = ''
    cadena = cadena + 'Codigo del estudiante... ' + str(e['codigo']) + '\n'
    cadena = cadena + 'Nombre... ' + e['nombre'] + '\n'
    cadena = cadena + 'sexo... ' + e['sexo'] + '\n'
    cadena = cadena + 'Edad... ' + str(e['edad']) + '\n'
    cadena = cadena + 'Notas... ' + str(e['notas']) + '\n'

    return(cadena)


def curso_como_cadena(curso: list) -> str:
    cadena = ""
    cadena = cadena + "|{:>3}".format("No")
    cadena = cadena + "|{:<6}".format("Código")
    cadena = cadena + "|{:<20}".format("Nombre")
    cadena = cadena + "|{:<7}".format("Genero")
    cadena = cadena + "|{:<5}".format("Edad")
    cadena = cadena + "|{:<20}".format("Notas")
    cadena = cadena + "\n"

    ne = len(curso)
    i = 0
    while(i < ne):
        e = curso[i]
        cadena = cadena + "|{:>3}".format(str(i))
        cadena = cadena + "|{:<6}".format(e["codigo"])
        cadena = cadena + "|{:<20}".format(e["nombre"])
        cadena = cadena + "|{:<7}".format(e["sexo"])
        cadena = cadena + "|{:<5}".format(e["edad"])
        cadena = cadena + "|{:<20}".format(str(e["notas"]))
        cadena = cadena + "\n"
        i = i+1

    return (cadena)


def calcular_definitiva(e: dict) -> float:
    w: list
    w = e["notas"]
    nd = len(w)
    rta = 0
    i = 0
    while(i < nd):
        rta = rta + w[i]
        i = i+1

    rta = rta/nd
    return(rta)


def mayor_nota(e: dict) -> float:
    nd = len(e["notas"])
    mayor = e["notas"][0]
    rta = 0
    i = 1
    while(i < nd):
        if(e["notas"][i] > mayor):
            mayor = e["notas"][i]
        i = i+1
    return(mayor)


"""Esta funcion cambia una nota de un estudiante mayor o igual a 4.5
   por 5.0 ó si es menor al valor evaluado anteriormente (menor a 4.5)
   solo adiciona 0.5 a dicha nota

   Parametros: (e:dict) Un diccionario (Registro de los datos de
                      un estudiante.)

   Retorno (None): Esta funcion es un procedimineto que realiza una
                   tarea sin retornar valor.
"""


def sumar_regalo(e: dict) -> None:
    n = e["notas"]
    nd = len(n)
    rta = 0
    i = 0
    while(i < nd):
        if(n[i] >= 4.5):
            n[i] = 5.0
        else:
            n[i] = n[i]+0.5
        i = i+1


"""Esta funcion obtiene la posicion del estudiante con la mayor definitiva

   Parametros: (list) Una array unidimensional (lista) que contiene los
   registros de los datos de los estudiantes.

   Retorno: (int) La posicion del estudiante con mayor definitiva   
"""


def pos_mayor_definitiva(x: list) -> int:
    ndx = len(x)
    mayor = calcular_definitiva(x[0])
    pos = 0
    k = 1
    while(k < ndx):
        d = calcular_definitiva(x[k])
        if(d > mayor):
            mayor = d
            pos = k
        k = k+1
    return (pos)


# haga y documente una funcion que retorne el registro del estudiante mas joven
def pos_menor_edad(x: list) -> int:
    ndx = len(x)
    menor = x[0]["edad"]
    pos = 0
    k = 1
    while(k < ndx):
        d = x[k]["edad"]
        if(d < menor):
            menor = d
            pos = k
        k = k+1
    return (pos)


def registro_mejor_nota_femenino(x: list) -> int:
    """
    Esta funcion retorna el registro de la mejor estudiante femenino en caso
    de que no exista una retorna None
    """
    mujeres_del_curso = mujeres(x)
    if len(mujeres_del_curso) == 0:
        return None
    ndx = len(mujeres_del_curso)
    mejor = calcular_definitiva(mujeres_del_curso[0])
    pos = 0
    k = 1
    while(k < ndx):
        if (calcular_definitiva(mujeres_del_curso[k]) > mejor):
            mejor = calcular_definitiva(mujeres_del_curso[k])
            pos = k
        k = k+1
    return (mujeres_del_curso[pos])


def mujeres(x: list) -> list:
    """
    Esta funcion retorna una lista con los registros de las mujeres del curso
    """
    ndx = len(x)
    rta = []
    k = 0
    while(k < ndx):
        if(x[k]["sexo"] == "F"):
            rta.append(x[k])
        k = k+1
    return (rta)


# funcion agregar estudiante que recibe el curso y los datos del estudiante como parametros
def agregar_estudiante_param(x: list, codigo: int, nombre: str, sexo: str, edad: int, notas: list, file: str) -> None:
    """
    Esta funcion agrega un estudiante al curso 
    """
    # validar que el codigo no exista en el curso
    ndx = len(x)
    k = 0
    while(k < ndx):
        if(x[k]["codigo"] == codigo):
            print("El codigo del estudiante ya existe")
            return
        k = k + 1

    nuevo_estudiante = {}
    nuevo_estudiante["codigo"] = codigo
    nuevo_estudiante["nombre"] = nombre
    nuevo_estudiante["sexo"] = sexo
    nuevo_estudiante["edad"] = edad
    nuevo_estudiante["notas"] = notas
    x.append(nuevo_estudiante)
    archivo = open(file, "a")
    archivo.write(str(nuevo_estudiante) + "\n")
    archivo.close()


def eliminar_un_estudiante(x: list, codigo: int, file: str) -> None:
    """
    Esta funcion elimina un estudiante del curso
    """
    ndx = len(x)
    k = 0
    while(k < ndx):
        if(x[k]["codigo"] == codigo):
            x.pop(k)
            break
        k = k + 1
    archivo = open(file, "w")
    for estudiante in x:
        archivo.write(str(estudiante) + "\n")
    archivo.close()


def eliminar_notas_inferiores_a_2(x: list, file: str) -> None:
    """
    Eliminar las notas menor a 2.0
    """
    ndx = len(x)
    k = 0
    while(k < ndx):
        i = 0
        nuevasNotas = []
        while(i < len(x[k]['notas'])):
            if (x[k]['notas'][i] >= 2):
                nuevasNotas.append(x[k]['notas'][i])
            i += 1
        x[k]['notas'] = nuevasNotas
        k += 1
    archivo = open(file, "w")
    k = 0
    while k < ndx:
        archivo.write(str(x[k]) + "\n")
        k += 1
    # for estudiante in x:
    #     archivo.write(str(estudiante) + "\n")
    archivo.close()


def dar_regalos_a_todos(datos: list) -> None:
    k = int(0)
    while(k < len(datos)):
        sumar_regalo(datos[k])
        k = k+1


def eliminar_notas(clase: list) -> None:
    nt: list
    j: int
    estudiante: dict
    k = int(0)

    while(k < len(clase)):
        j = 0
        estudiante = clase[k]
        nt = estudiante["notas"]
        while(j < len(nt)):
            if(nt[j] < 2):
                nt.pop(j)
            j = j+1

        k = k+1


# area de pruebas
curso = traer_de_archivo('data.txt')
print(curso_como_cadena(curso))
p = pos_mayor_definitiva(curso)
print("posición mayor definitiva:", p)
print('----------------------------')
print(estudiante_como_cadena(curso[p]))
print(calcular_definitiva(curso[3]))
print(mayor_nota(curso[4]))
sumar_regalo(curso[5])
print(curso_como_cadena(curso))
dar_regalos_a_todos(curso)
print(curso_como_cadena(curso))
eliminar_notas(curso)
print(curso_como_cadena(curso))
mas_joven = pos_menor_edad(curso)
print("posición menor edad:", mas_joven)
print('----------------------------')
print(estudiante_como_cadena(curso[mas_joven]))
print("Mejor nota femenina")
print('----------------------------')
print(estudiante_como_cadena(registro_mejor_nota_femenino(curso)))
agregar_estudiante_param(curso, 123, "Juan", "M", 20,
                         [1, 2, 3, 4, 5], "data.txt")
eliminar_un_estudiante(curso, 8921, "data.txt")
eliminar_notas_inferiores_a_2(curso, "data.txt")
