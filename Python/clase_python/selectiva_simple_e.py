'''
selectiva_simple_e.py
script en Python que implementa un sistema de redondeo de
calificaciones- El usuario es el encargado de ingresar su calificación.
Si a la calificación le faltan 4 unidades o menos
para el siguiente multiplo de 10, entonces su calificación será
redondeada al siguiente multiplo de 10, en caso
contrario la calificación no es modificada. 
Ejemplo.
Si el usuario obtuvo 76 entonces se redondea a 80
Si el usuario obtuvo 75 entonces su calificación es 75
una sentencia if
'''

calificacion = int(input('¿Cuá es tu calificación?: '))

if 0<= calificacion <= 100 and calificacion%10 >=6:
    calificacion = (calificacion//10 + 1) * 10
print(f'Tu puntaje es {calificacion}')