estudiantes=[[0,0],[0,0],[0,0],[0,0],[0,0]]
notas_estudiantes=[[0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0]]
porcentajes=[[0.15,0.20],[0.15,0.20],[0.10,0.20]]

VALOR_PARCIAL = 0.20
VALOR_TRABAJOS_1_2 = 0.15
VALOR_TRABAJOS_3 = 0.10

indicador_matricula=0
cargar_informacion=0
nota_definitiva=0
cont=0
estudiante=0
while True:
    print('''      MENÚ
    1. Cargar Notas
    2. Buscar Notas
    3. Salir''')
    op=int(input('Selecciona una opción del menú anterior: '))
    go_back=False
    if op==1:
        while True:
            if go_back:
                break
            print('''MENÚ
            1.Matricular
            2.Cargar Información
            3.Retornar al menú anterior
            ''')
            op=int(input('Selecciona una opción: '))
            if op == 3:
                go_back = True
                continue
            if op==1:
                if indicador_matricula==1:
                    print('Los alumnos se encuentran matriculados, intente nuevamente')
                else:
                    contador=0
                    while contador<=4 :
                        estudiantes[contador][0]=input( f'Nombre del estudiante #{contador+1} a matricular: ')
                        estudiantes[contador][1]=int(input(f'Ingresa la cédula del estudiante #{contador+1}: '))
                        contador+=1
                    indicador_matricula=1
            elif op==2 and cargar_informacion==0:
                c_1=0
                c_2=0
                c_3=0
                n_estudiante=0
                n_corte=0
                while True:
                    if go_back:
                        break
                    while estudiante < 5:
                        if go_back:
                            break
                        nota_del_15=0
                        nota_del_20=0
                        print('''MENÚ
                        1. Corte 1
                        2. Corte 2
                        3. Corte 3
                        4. Retornar al menú anterior''')
                        print('Ingresando notas del estudiante #',estudiante+1)
                        while True:
                            op=int(input('Seleccione una opción: '))
                            if op==4:
                                go_back = True
                                break
                            if op > 4 or op < 1:
                                print('Ingrese una opción incorrecta,vuelva a intentarlo')
                                break
                            if op==1 and c_1==0:
                                c_1=1
                                n_corte=1
                                break
                            if op==2 and c_2==0 and c_1==1:
                                c_2=1
                                n_corte=2
                                break
                            if op==3 and c_3==0 and c_2==1 and c_1==1:
                                c_3=1
                                n_corte=3
                                break
                        contador=0
                        if go_back:
                            break
                        print('Ingresando notas del corte #',n_corte)
                        while contador<=3:
                            if c_1==1 or c_2==1 or c_3==1 :
                                if contador<3:
                                    notas_estudiantes[estudiante][n_estudiante]=float(input(f'Ingrese la nota del Quiz #'))
                                    if (c_1==1 or c_2==1) and c_3==0:
                                        nota_del_15 += (notas_estudiantes[estudiante][n_estudiante]/3)*VALOR_TRABAJOS_1_2
                                    elif c_1==1 and c_2==1 and c_3==1:
                                        nota_del_15+= (notas_estudiantes[estudiante][n_estudiante]/3)*VALOR_TRABAJOS_3
                                else:
                                    notas_estudiantes[estudiante][n_estudiante]=float(input(f'Ingrese la nota del Parcial: '))
                                    nota_del_20 += notas_estudiantes[estudiante][n_estudiante]*VALOR_PARCIAL
                                n_estudiante += 1
                                contador+=1
                            else:
                                print("Datos invalidos")
                                break
                        POS_DEFINITIVA = 12
                        notas_estudiantes[estudiante][POS_DEFINITIVA] += nota_del_20 + nota_del_15
                        print("Nota definitiva actual: ", notas_estudiantes[estudiante][POS_DEFINITIVA])
                    estudiante +=1
    elif op==2:
            cc=int(input("cedula del estudiante a buscar"))
            indice = 0
            for est in estudiantes:
                if est[1] == cc:
                    print("Nombre:", est[0])
                    print("Cedula:", est[1])
                    break
                indice += 1
            indice_notas = 0
            for notas_estudiante in notas_estudiantes:
                if indice_notas == indice:
                    print(notas_estudiante)
                indice_notas += 1