'''
procedimientos_6.py
Script en Python que implemente un procedimiento que reciba el nombre
y la edad del usuario y en caso que la edad sea mayor o igual que 18
le indique que ya es mayor de edad; en caso contrario le indique que es
menor de edad.
'''

def mayoria__edad(nombre, edad):
    print(f'Hola {nombre} un gusto verte de nuevo')
    if edad >= 18:
        print(f'Ya eres mayor de edad, {nombre}')
    else:
        print(f'Aún eres menor, {nombre}')
name = input('Hola, ¿Comó te llamas?: ')
age = int(input('¿Cuál es tu edad?: '))
mayoria__edad(name, age)

print('Nos vemos...')