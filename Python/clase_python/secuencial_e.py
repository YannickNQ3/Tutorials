'''
Secuencial_e1.py
script en Python que calcule el área de un triangulo.
El usuario deberá ingresar tanto el valor de 
la base como el de la altura y el programa 
mostrará el valor de el área.
'''

base = float(input('Ingresa la base del triangulo: '))
altura = float(input('Ingresa la altura del triangulo: '))

area = (base * altura)/2

print(f'El área del triangulo de base {base} y altura {altura} es: {area}')