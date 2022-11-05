'''
repetitiva_desde_5.py
script en Python que muestre las tablas de multiplicar de los números
del 1 al 10. Cada tabla se muestra hasta el decímo multiplo 
'''
import os
for numero in range(1,11):
    os.system('cls')
    print(f'        Tabla de multiplicar del {numero}')
    for multiplo in range(1,11):
        print(f'{numero} X {multiplo} = {numero * multiplo}')
    input('Presione enter para continuar...')
print('Nos vemos...')
