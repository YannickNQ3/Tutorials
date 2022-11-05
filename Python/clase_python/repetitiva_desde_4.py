'''
repetitiva_desde_4.py
Script en Python que muestre la tabla de multiplicar de un número
ingresado por el usuario. El usuario también podrá ingresar hasta 
que valor llegar'a la tabla de multiplicar
'''

numero = int(input('¿De que número deseas ver la tabla de multiplicar? '))
limite = int(input('¿Hasta que multiplo deseas ver? '))
print(f'            Tabla del {numero}')
for multiplo in range(1, limite+1):
    print(f'{numero} X {multiplo} = {numero*multiplo}')
print('Nos vemos...')