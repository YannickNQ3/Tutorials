'''
repetitiva_mientras_3.py
script en Python que simule el sistema de validación de datos 
de una plataforma digital. Se le solicitará al usuario su nombre
y contraseña mientras la información proporcionada no coincida con la 
información previamente registrada.
'''
import os

USER = 'pepe_nava'
PASSWORD = 'v1dr1o'

user = ''
password = ''

while USER != user or PASSWORD != password:
    os.system('cls')
    print('     KIT - KOT')
    user = input('Usuario: ')
    password = input('Contraseña: ')

    if USER != user or PASSWORD != password:
        print('Credenciales Incorrectas')
        print('Intenta de nuevo')
        input('Presiona enter para continuar')
else:
    print('Bienvenid@')
input('Nos vemos')