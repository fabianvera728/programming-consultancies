numero_de_notas = 3
acumulado_notas = 0
id_corte=0
CORTE_1 = 0
CORTE_2 = 1
CORTE_3 = 2
nombre=input("digite su nombre:")
codigo=input("digite su codigo:")
while(id_corte<=2):
    print("corte #:",id_corte+1)
    nota1=float(input("ingrese la quiz1:"))
    nota2=float(input("ingrese la quiz2:"))
    nota3=float(input("ingrese la quiz3:"))
    nota_parcial=float(input("ingrese la parcial:"))
    sumatoria_notas = nota1 + nota2 + nota3
    if id_corte == CORTE_1 or id_corte == CORTE_2:
        definitiva_trabajos = ((sumatoria_notas/numero_de_notas) * 0.15)
    elif id_corte== CORTE_3:
        definitiva_trabajos = ((sumatoria_notas/numero_de_notas) * 0.10)
    definitiva_parcial = (nota_parcial * 0.20)
    nota_final = definitiva_trabajos + definitiva_parcial 
    acumulado_notas += nota_final
    id_corte += 1
    print("la nota definitiva del corte es:", nota_final)

print("Su nota final es:", acumulado_notas)
