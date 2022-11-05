'''
funciones_3.py
Script en Python que implemente una función encargada de convertir
gradps Fahrenheit a Celsius.
'''

def fahrenheit_a_celcius():
    f = float(input('Grado Fahrenheit: '))
    c = (f-32)/1.8
    return c

print('Programa que convierte grados Fahrenheit a Celcius')
celcius = fahrenheit_a_celcius()
print(f'Celcius: {celcius :.2f}')

print('Nos vemos...')