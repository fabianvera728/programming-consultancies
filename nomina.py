# SMMLV 877803 (2020)
# Los datos iniciales corresponden a CEDULA, SUELDO, DIAS TRABAJADOS
# Se contrata a la persona por un sueldo cuyo minimo seria el SMMLV
# Campos calculados
# • VALOR DÍA TRABAJADO = Salario Base / días del mes.
# • SALARIO BÁSICO = días trabajados * Valor día trabajado.
# • REMUNERACION es igual a $50.000, esto si los trabajadores ganan menos de 1,5 SMLV.
# • SUBSIDIO DE TRANSPORTE es el 2% y SUBSIDIO DE ALIMENTACIÓN 3% del sueldo,
# esto si los trabajadores ganan menos de 2 SMMLV.
# • TOTAL DEVENGADO = Salario Básico + Remuneración + subsidio de transporte + subsidio de alimentación.
# • SALUD = 4% y PENSION = 4,5% del salario básico.
# • DESCUENTO el 1% del salario básico, esto si los trabajadores ganan mas de 2 SMLV.
# • TOTAL DEDUCIDO = SALUD + PENSION + DESCUENTO
# • SALARIO FINAL = Total Devengado – Total Deducido.
# • SUBTOTAL DE NOMINA = SUMATORIA DE SALARIOS FINALES
# • CALCULAR EL TOTAL DE NOMINA agregando los siguientes parafiscales
# SENA= 2%, ICBF = 3% Y CCF = 4%,

# -IMPRIMA LA NOMINA UNA VEZ HALLA CALCULADO TODOS SUS CAMPOS
# -IMPRIMA EL SUBTOTAL DE NOMINA
# -IMPRIMA EL TOTAL DE NOMINA
# A=[[88453521,2050000,23,0,0,0,0,0,0,0,0],
# [74321041,1260000,15,0,0,0,0,0,0,0,0]]

# El salario base SMLV = 877803

SMLV = 877803
# • VALOR DÍA TRABAJADO = Salario Base / días del mes.


def valor_dia_trabajado(salario_base, dias_trabajados):
    return salario_base / dias_trabajados
# • SALARIO BÁSICO = días trabajados * Valor día trabajado.


def salario_basico(dias_trabajados, valor_dia_trabajado):
    return dias_trabajados * valor_dia_trabajado
# • REMUNERACION es igual a $50.000, esto si los trabajadores ganan menos de 1,5 SMLV.


def remuneracion(salario_basico):
    if salario_basico < SMLV * 1.5:
        return 50000
    else:
        return 0
# • SUBSIDIO DE TRANSPORTE es el 2% y SUBSIDIO DE ALIMENTACIÓN 3% del sueldo, esto si los trabajadores ganan menos de 2 SMMLV.


def subsidio_transporte(salario_basico):
    if salario_basico < SMLV * 2:
        return salario_basico * 0.02
    else:
        return 0


def subsidio_alimentacion(salario_basico):
    if salario_basico < SMLV * 2:
        return salario_basico * 0.03
    else:
        return 0

# • TOTAL DEVENGADO = Salario Básico + Remuneración + subsidio de transporte + subsidio de alimentación.


def total_devengado(salario_basico, remuneracion, subsidio_transporte, subsidio_alimentacion):
    return salario_basico + remuneracion + subsidio_transporte + subsidio_alimentacion

# • SALUD = 4%


def salud(salario_basico):
    return salario_basico * 0.04

# * PENSION = 4,5% del salario básico.


def pension(salario_basico):
    return salario_basico * 0.045


# • DESCUENTO el 1% del salario básico, esto si los trabajadores ganan mas de 2 SMLV.


def descuento(salario_basico):
    if salario_basico > SMLV * 2:
        return salario_basico * 0.01
    else:
        return 0
# • TOTAL DEDUCIDO = SALUD + PENSION + DESCUENTO


def total_deducido(salud, pension, descuento):
    return salud + pension + descuento
# • SALARIO FINAL = Total Devengado – Total Deducido.


def salario_final(total_devengado, total_deducido):
    return total_devengado - total_deducido
# • SUBTOTAL DE NOMINA = SUMATORIA DE SALARIOS FINALES


def subtotal_nomina(nomina: list):
    subtotal = 0
    for empleado in nomina:
        subtotal += empleado[13]
    return subtotal
# • CALCULAR EL TOTAL DE NOMINA agregando los siguientes parafiscales
# SENA= 2%, ICBF = 3% Y CCF = 4%,


def total_nomina(subtotal_nomina):
    return subtotal_nomina + (subtotal_nomina * 0.02) + (subtotal_nomina * 0.03) + (subtotal_nomina * 0.04)


# -IMPRIMA LA NOMINA UNA VEZ HALLA CALCULADO TODOS SUS CAMPOS
# -IMPRIMA EL SUBTOTAL DE NOMINA
# -IMPRIMA EL TOTAL DE NOMINA
# A=[[88453521,2050000,23,0,0,0,0,0,0,0,0],1260000.0
# [74321041,1260000,15,0,0,0,0,0,0,0,0]]

# A =[["cedula", "salario_base", "diasttrabajados", "vdiat", "salariobasico", "remuneracion", "subsidiotransporte",
# "subsidioalimentacion", "totaldevengado", "salud", "pension", "descuento", "totaldeducido", "salariofinal", "subtotalnomina"],
# [88453521,2050000,23,0,0,0,0,0,0,0,0],

def calcular_nomina(empleados: list) -> list:
    i = 0
    while i < len(empleados):
        empleados[i][3] = valor_dia_trabajado(empleados[i][1], empleados[i][2])
        empleados[i][4] = salario_basico(empleados[i][2], empleados[i][3])
        empleados[i][5] = remuneracion(empleados[i][4])
        empleados[i][6] = subsidio_transporte(empleados[i][4])
        empleados[i][7] = subsidio_alimentacion(empleados[i][4])
        empleados[i][8] = total_devengado(
            empleados[i][4], empleados[i][5], empleados[i][6], empleados[i][7])
        empleados[i][9] = salud(empleados[i][4])
        empleados[i][10] = pension(empleados[i][4])
        empleados[i][11] = descuento(empleados[i][4])
        empleados[i][12] = total_deducido(
            empleados[i][9], empleados[i][10], empleados[i][11])
        empleados[i][13] = salario_final(empleados[i][8], empleados[i][12])
        i += 1

    return empleados


def imprimir_nomina(empleados: list) -> None:
    i = 0
    while i < len(empleados):
        print(empleados[i][0], end="\t")
        print(empleados[i][1], end="\t")
        print(empleados[i][2], end="\t")
        print(empleados[i][3], end="\t")
        print(empleados[i][4], end="\t")
        print(empleados[i][5], end="\t")
        print(empleados[i][6], end="\t")
        print(empleados[i][7], end="\t")
        print(empleados[i][8], end="\t")
        print(empleados[i][9], end="\t")
        print(empleados[i][10], end="\t")
        print(empleados[i][11], end="\t")
        print(empleados[i][12], end="\t")
        print(empleados[i][13], end="\n")
        i += 1


# area de pruebas
NOMINA_SIN_CALCULAR = [
    [74321041, 1260000, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [74321041, 1260000, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [74321041, 1260000, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [74321041, 1260000, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
nomina = calcular_nomina(NOMINA_SIN_CALCULAR)
imprimir_nomina(nomina)
subtotal = subtotal_nomina(nomina)
print("Este es el subtotal de la nomina: ", subtotal)
print("Este es el total de la nomina: ", total_nomina(subtotal))
