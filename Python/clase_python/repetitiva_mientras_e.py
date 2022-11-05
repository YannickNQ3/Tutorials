'''
repetitiva_mientras_e.py
Script en Python que implemente el juego de adivinar un número,
pero esta vez en modo competitivo. La computadora deberá generar
un numero aleatorio entre 1 y 100 y tanto el usuario como la 
computadora deberán intentar adivinar dicho número. Para que el
juego sea retador el jugador maquina deberá ser "inteligente" y
competir para ganar. El juego se realizará por turnos, primero la
máquina y después el usuario y por cada intento la computadora 
responderá si el número es mayor o menor que el secreto.
'''
import random
import os
inferior = 1
superior = 100
secreto = random.randint(1, 100)
maquina = -1
usuario = -1
while usuario != secreto and maquina != secreto:
    os.system('cls')
    print('Maquina, ¿Cual crees que sea el numero secreto?')
    maquina = random.randint(inferior, superior)
    print(f'Maquina: {maquina}')
    if maquina <secreto:
        print('Tu número es menor')
        inferior = maquina + 1
    elif maquina > secreto:
        print('tu numero es mayor: ')
        superior = maquina - 1
    else: 
        print('Maquina Gana')
    if maquina != secreto:
        usuario = int(input('Usuario, ¿Cual crees que sea el numero secreto? '))
        if usuario <secreto:
            print('Tu número es menor')
            if usuario > inferior:
                inferior = usuario + 1
        elif usuario > secreto:
            print('tu numero es mayor: ')
            if usuario < superior:
                superior = usuario - 1
        else: 
            print('Usuario Gana')
    input('Presiona enter para continuar..-')
input('Nos vemos...')