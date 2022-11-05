'''
repetitiva_mientras_2.py
script en Python que sume valores pares y multiplique valores impares
mientras el usuario no ingrese un 0. Se deberá utilizar la estructura
repetitiva "while" para solicitar al usuario un número y dependiendo del 
número lo suma o lo multiplica
'''

print('Programa que suma lso números pares y multiplica los impares')

suma = 0
multiplicación = 1
numero = -1
while numero != 0:
    numero = int(input('Ingresa un numero (0 para salir)'))
    if numero % 2 == 0:
        suma = suma + numero
    else:
        multiplicación = multiplicación * numero

    print(f'Suma: {suma}')
    print(f'Multiplicación: {multiplicación}')
print('Nos vemos')