# c)cree una funcion que detecte la posicion de la persona mas joven e insete el siguiente dato "magdalena",44
# d)cree una funcion que elimine a la persona mas joven de la lista


def obtener_posicion_persona_mas_joven(personas):
    i = 1
    pos_menor = i
    valor_menor = personas[i]
    while(i < len(personas)):
        if (valor_menor > personas[i]):
            valor_menor = personas[i]
            pos_menor = i
        i += 2
    return pos_menor - 1


def cambiar_persona_mas_joven(personas):
    persona_menor = obtener_posicion_persona_mas_joven(personas)
    personas[persona_menor] = "magdalena"
    personas[persona_menor+1] = 44


def eliminar_persona_mas_joven(personas: list):
    persona_menor = obtener_posicion_persona_mas_joven(personas)
    personas.pop(persona_menor)
    personas.pop(persona_menor)


# area de prueba
personas = ["pedro", 12, "maria", 14, "judas",
            17, "pablo", 18, "juan", 19, "jesus", 10]
# cambiar_persona_mas_joven(personas)
eliminar_persona_mas_joven(personas)
print(personas)
