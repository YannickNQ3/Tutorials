'''
funciones_4.py
Script en Python que implemente una función para calcular el área
de un triangulo. Dicha función debera recibir como argumentos el valor de
la base y la altura y regresará el área calculada.
'''

def area_triangulo(altura, base):
    return base * altura / 2

print('Programa que calcula el area de un triangulo')
print('Ingresa los siguientes datos')
Altura = float(input('Altura: '))
base = float(input('Base: '))

print(f'Área = {area_triangulo(Altura, base) :.2f}')

print('Nos vemos...')