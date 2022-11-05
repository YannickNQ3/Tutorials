'''
procedimientos_5.py
script en Python que implemente un procedimiento que reciba el nombre 
del usuario como argumento e imprima un saludo personalizado.

'''
def saludo(nombre):
    print(f'Hola {nombre}, gusto en concerte')
n = input('¿Cómo te llamas?: ')
saludo(n)
saludo('Lucy')
print('Nos vemos...')