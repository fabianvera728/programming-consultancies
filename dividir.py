def obtener_digitos_numero(numero: int) -> list:
    digitos = []
    while numero // 10 > 0:
        digitos.append(numero % 10)
        numero = numero // 10
    digitos.append(numero)
    digitos.reverse()
    return digitos


def generar_estructura_respuesta(digitos: list) -> dict:
    respuesta = {}
    i = 0
    while i < len(digitos):
        respuesta[digitos[i]] = ""
        i += 1

    return respuesta


def es_pica_o_es_fija(digitos: list, respuesta_actual: dict,
                      numero: int, posicion_a_ingresar: int):
    if numero not in digitos:
        return
    if not (posicion_a_ingresar >= 1 and posicion_a_ingresar <= len(digitos)):
        print("posicion no valida")
        return
    posicion_numero_en_los_digitos = digitos.index(numero)
    if (posicion_a_ingresar - 1) == posicion_numero_en_los_digitos:
        respuesta_actual[numero] = 'fija'
    else:
        respuesta_actual[numero] = 'pica'

# area de pruebas


def main():
    digitos = obtener_digitos_numero(4321)
    estructura_respuesta = generar_estructura_respuesta(digitos)
    es_pica_o_es_fija(digitos, estructura_respuesta, 1, 4)
    print(estructura_respuesta)


main()


[https://hola.py](https://hola.py)
[https://hola.java](https://hola.java)
[https://hola.js](https://hola.js)
[https://hola.c](https://hola.c)
[https://hola.r](https://hola.r)
[https://hola.cpp](https://hola.cpp)





