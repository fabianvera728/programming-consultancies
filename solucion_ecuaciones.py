# funcion para resolver el siguiente sistema de ecuaciones lineales utilizando matrices para su representacion y solucion
# a)  2 x - 2y + z = 1
# b)  -x + y + z = 0
# c)  -x + 3y + 5z = 0
# resolver_sistema([[2, -2, 1], [-1, 1, 1], [-1, 3, 5]], [1, 0, 0])

import numpy as np

# Método de Gauss-Jordan
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B


def resolver_sistema(A, B):

    # PROCEDIMIENTO
    # casicero = 1e-15  # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A, dtype=float)

    # Matriz aumentada
    AB = np.concatenate((A, B), axis=1)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0, n-1, 1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:, i])
        dondemax = np.argmax(columna)

        # dondemax no está en diagonal
        if (dondemax != 0):
            # intercambia filas
            temporal = np.copy(AB[i, :])
            AB[i, :] = AB[dondemax+i, :]
            AB[dondemax+i, :] = temporal

    # eliminacion hacia adelante
    for i in range(0, n-1, 1):
        pivote = AB[i, i]
        adelante = i + 1
        for k in range(adelante, n, 1):
            factor = AB[k, i]/pivote
            AB[k, :] = AB[k, :] - AB[i, :]*factor

    # elimina hacia atras
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila, 0-1, -1):
        pivote = AB[i, i]
        atras = i-1
        for k in range(atras, 0-1, -1):
            factor = AB[k, i]/pivote
            AB[k, :] = AB[k, :] - AB[i, :]*factor
        # diagonal a unos
        AB[i, :] = AB[i, :]/AB[i, i]
    X = np.copy(AB[:, ultcolumna])
    X = np.transpose([X])
    return X


def main():
    # INGRESO
    A = np.array([[2, -2, 1],
                  [-1, 1, 1],
                  [-1, 3, 5]])

    B = np.array([[1],
                  [0],
                  [0]])

    print("Sistema de ecuaciones:")
    print(A)
    print(B)
    print("Solución:")
    X = resolver_sistema(A, B)
    # imprimir x y y z
    print("x =", X[0, 0], "y =", X[1, 0], "z =", X[2, 0])


if __name__ == "__main__":
    main()
# main()
# SALIDA
# print('Matriz aumentada:')
# print(AB0)
# print('Pivoteo parcial por filas')
# print(AB1)
# print('eliminacion hacia adelante')
# print(AB2)
# print('eliminación hacia atrás')
# print(AB)
# print('solución de X: ')
# print(X)
