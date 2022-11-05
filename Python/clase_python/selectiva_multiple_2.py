'''
Selectiva_multiple_2.py
script en Python que muestre un menú con los
nombres distintos de Paises de América y si
el usuario selecciona alguna de las opciones
se le mostrará el nombre de la capital
de ese país.
'''
MEXICO = 1
URUGUAY = 2
COLOMBIA = 3
ARGENTINA = 4
ECUADOR = 5
PERU = 6
print('''           Capitales de América
1) México
2) Uruguay
3) Colombia
4) Argentina
5) Ecuador
6) Perú
''') 
opc = int(input('Selecciona una opción: '))

if opc == MEXICO:
    print('Ciudad de Mexico')
elif opc == URUGUAY:
    print('Montevideo')
elif opc == COLOMBIA:
    print('Bogotá')
elif opc == ARGENTINA:
    print('Buenos Aires')
elif opc == ECUADOR:
    print('Quito')
elif opc == PERU:
    print('Lima')
else:
    print('Opción no válida')
print('Que tengas un buen día')