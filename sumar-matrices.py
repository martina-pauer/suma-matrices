#!/usr/bin/python3

import string

def sumar(matriz_1:list, matriz_2:list) -> list:
    '''
        Devuelve suma de dos listas bidimensionales (lista con listas de misma longitud adentro).
        solo sirve para matrices con igual cantidad de filas y columnas
    '''
    # Analiza cuantas filas y columnas tienen las listas bidimensionales
    filas = len(matriz_1)

    columnas = len(matriz_1[0])    
    # Recorro matriz con indexado de elementos voy sumando items a matriz resultado
    for columna in range(columnas):
        for fila in range(filas):
            print('\nSumando Fila: ', fila, ' Columna: ', columna, '\n')
            if matriz_2[fila][columna].__str__() in string.digits:
                matriz_2[fila][columna] = int(matriz_2[fila][columna]) + int(matriz_1[fila][columna])

    print('\t Resultado: ', matriz_2, '\n')

    return matriz_2

def matriz(inicio:int, linea_de_corte:int) -> list:
    '''
        Devuelve lista bidimensional con
        valores numericos antes de linea
        de corte en archivo 'matrices.txt'.
    '''
    archivo = open('matrices.txt', 'r')

    lineas = archivo.readlines()[inicio - 1:linea_de_corte]
    
    resultado = []

    for linea in lineas:
        if linea[0] in string.digits:
            resultado.append(list(linea.replace(' ', '').replace('\n', '')))
    # Evita memory leaks por overflow
    archivo.close()
    # Convierto numero de resultado en enteros
    for fila in resultado:
        for numero in range(len(fila)):
            fila[numero] = int(fila[numero])

    return resultado

sep = '-' * 30
# Seguir bien el formato de archivos
primera = matriz(1, 3)

segunda = matriz(3, 6)
# Escribo contenido al archivo suma-dos-matrices.txt
salida = open('suma-dos-matrices.txt', 'w')

contenido = ''

contenido += ('\n\t' + primera.__str__() + '\n\n\t' + segunda.__str__())

contenido += ('\n\n ' + sep + ' Suman ' + sep + '\n\n\t\t' + sumar(primera, segunda).__str__() + '\n')

salida.write(contenido)
# Cierro la salida para evitar memory leaks por guardar en memoria referencia de acceso a archivo
salida.close()
