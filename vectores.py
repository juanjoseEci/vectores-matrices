'''
    2/13/22 laboratorio  operaciones vectores complejos
    Juan José Álvarez Beltrán
'''
##Adición de vectores complejos.
##Inverso (aditivo) de un vector complejo.
##Multiplicación de un escalar por un vector complejo.
##Adición de matrices complejas.
##Inversa (aditiva) de una matriz compleja.
##Multiplicación de un escalar por una matriz compleja.
##Transpuesta de una matriz/vector
##Conjugada de una matriz/vector
##Adjunta (daga) de una matriz/vector
##Producto de dos matrices (de tamaños compatibles)
##Función para calcular la "acción" de una matriz sobre un vector.
##Producto interno de dos vectores
##Norma de un vector
##Distancia entre dos vectores
##Revisar si una matriz es unitaria
##Revisar si una matriz es Hermitiana
##Producto tensor de dos matrices/vectores

import numpy as np
def comprobacion_columnas(matriz_vtor):
    try:
        column = len(matriz_vtor[0])
        return column
    except TypeError:
        column = 1
        return column
def comprobacion_booleano(matriz_vtor):
    try:
        len(matriz_vector[0])
        return True
    except TypeError:
        return False
def conjugado_complejos(num_complejo):
    real = num_complejo.real
    imag = -1 * num_complejo.imag
    if imag == 0:
        imag = 0
    if imag < 0:
        num = str(real) + str(imag) + 'j'
    else:
        num = str(real) + '+' + str(imag) + 'j'
    return complex(num)
def suma_vtor(vector_1, vector_2):
    for i in range(len(vector_1)):
        vector_1[i] = vector_1[i] + vector_2[i]
    return vector_1[:]

def inverso_vtor(vector):
    for i in range(len(vector)):
        vector[i] = -1 * vector[i]
    return vector[:]
def escalar_vcomplejo(vector, escalar):
    for i in range(len(vector)):
        vector[i] = escalar * vector[i]
    return vector[:]
def suma_mtriz(vector_1, vector_2):
    filas = len(vector_1)
    columnas = len(vector_1[0])
    for i in range(filas):
        for j in range(columnas):
            vector_1[i][j] = vector_1[i][j] + vector_2[i][j]
    return vector_1[:]
def inverso_mtriz(matriz):
    matriz = [[-1 * matriz[j][k] for k in range(len(matriz[0]))] for j in range(len(matriz))]
    return matriz[:]
def escalar_mcomplejo(matriz, escalar):
    matriz = [[escalar * matriz[j][k] for k in range(len(matriz[0]))] for j in range(len(matriz))]
    return matriz[:]
def traspuesta_mtriz_vtor (matriz_vtor):
    filas = len(matriz_vector)
    columnas = comprobacion_columnas(matriz_vtor)
    if comprobacion_booleano(matriz_vtor):
        comp = [[matriz_vtor[k][j] for k in range(filas)] for j in range(columnas)]
        comp = (comp[0] if len(comp) == 1 else comp)
    else:
        comp = [[matriz_vtor[j] for k in range(columnas)] for j in range(filas)]
    return comp
def conjugado_mtriz_vtor(matriz_vtor):
    filas = len(matriz_vtor)
    columnas = comprobacion_columnas(matriz_vtor)
    if comprobacion_booleano(matriz_vtor):
        for j in range(filas):
            for k in range(columnas):
                matriz_vtor[j][k] = conjugado_complejos(matriz_vtor[j][k])
    else:
        for j in range(filas):
            matriz_vtor[j] = auxiliar_2(matriz_vtor[j])
    return matriz_vtor[:]
def adjunta_mtriz_vtor (matriz_vtor):
    return traspuesta_mtriz_vtor(conjugado_mtriz_vtor(matriz_vtor))
def multplicacion_mtriz (matriz_a, matriz_b):
    filas_a, filas_b, columnas_a, columnas_b = len(matriz_a), len(matriz_b), comprobacion_columnas(matriz_acomprobacion_columnas(matriz_b)
    if filas_b == columnas_a:
        comp = [[0 for i in range(columnas_b)] for j in range(filas_a)]
        for h in range(columnas_b):
            for j in range(filas_a):
                for k in range(columnas_a):
                    comp[j][h] += matriz_a[j][k] * matriz_b[k][h]
        return comp
    else:
        return 'error , no operable'
def accion(matriz, vector):
    filas, columnas, tamaño = len(matriz), len(matriz[0]), len(vector)
    comp = [0 for i in range(filas)]
    for j in range(filas):
        for k in range(columnas):
            comp[j] += matriz[j][k] * vector[k]
    return comp
def producto_punto (vector_a, vector_b):
    tamaño = len(vector_a)
    try:
        for i in range(tamaño):
            int(vector_a[i])
        suma = 0
        for j in range(tamaño):
            suma += vector_a[j] * vector_b[j]
        return suma
    except TypeError:
        vector_a = conjugado_mtriz_vtor(vector_a[:])
        suma = 0
        for j in range(tamaño):
            suma += complex(vector_a[j]) * complex(vector_b[j])
        return suma
def norma_vector(vector):
    try:
        for i in range(len(vector)):
            int(vector[i])
        return (producto_punto(vector[:], vector[:]))**(1/2)
    except TypeError:
        return (producto_punto(vector[:], vector[:]))**(1/2)
def disVectors(vector_a, vector_b):
    vector = suma_vtor(inverso_vtor(vector_a), vector_b)
    return norma_vtor(vector)
def hermitiana_mtriz(matriz):
    matriz_a = conjugado_mtriz_vtor(traspuesta_mtriz_vtor(matriz[:]))
    if matriz_a == matriz:
        return True
    else:
        return False
def unitaria_mtriz(matriz):
    size = len(matriz)
    identidad = [[(1 if j == k else 0) for k in range(tamaño)]for j in range(tamaño)]
    matriz = multMatrices(matriz, conjugado_mtriz_vtor(traspuesta_mtriz_vtor(matriz[:])))
    if matriz == identidad:
        return True
    else:
        return False
def tensor(matriz_vector_0,matriz_vector_1):
    filas_0, columnas_0, valor = len(matriz_vector_0), comprobacion_columnas(matriz_vector_0), comprobacion_booleano(matriz_vector_1)
    if columnas_0 == 1 and valor:
        for j in range(filas_0):
            matriz_vector_0[j] = multplicacion_mtriz(matriz_vector_1[:], matriz_vector_0[j])
    elif columnas_0 == 1:
        for j in range(filas_0):
            matriz_vector_0[j] = multplicacion_vtor(matriz_vector_1[:], matriz_vector_0[j])
    elif columnas_0 != 1 and valor:
        for j in range(filas_0):
            for k in range(columnas_0):
                matriz_vector_0[j][k] = multplicacion_mtriz(matriz_vector_1[:], matriz_vector_0[j][k])
    else:
        for j in range(filas_0):
            for k in range(columnas_0):
                matriz_vector_0[j][k] = multplicacion_vtor(matriz_vector_1[:], matriz_vector_0[j][k])
    return matriz_vector_0[:]
