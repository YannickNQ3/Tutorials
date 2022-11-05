'''
repetitiva_desde_2.py
Script en Python que imprima los números pares desde el 2 hasta el 20 haciendo
uso de un ciclo for.
'''

print('Programa que muestra los numeros pares desde el 2 hasta el 20')

print('Método 1')

for par in range (1,11):
    print(f'par: {par*2}')
print('*'*20)
print('Método 2')
for par in range (1,21):
    if par%2==0:
        print(f'par: {par}')
print('*'*20)
print('Método 3')
for par in range (2,21, 2):
    print(f'par: {par}')
print('Nos vemos...')

