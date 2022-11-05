'''
repetitiva_mientras_4.py
Script en Python que muestre un menú con distintos personajes
de un videojuego. Si el usuario seleccion alguno de los personajes, 
se le mostrarán sus caracteristicas. El menú será ciclico y se mostrará
mientras el usuario no indique que desea salir.
'''
import os

MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 4
#bandera
continuar = True
while continuar:
    os.system('cls')
    print(f'''          PERSONAJES
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir
    ''')

    opc = int(input('Selecciona tu personaje: '))

    if opc == MAGO:
        print('''
        Fuerza: 15
        Energia: 20
        Especial: 12
        ''')
    elif opc == GUERRERO:
        print('''
        Fuerza: 25
        Energia: 18
        Especial: 10
        ''')
    elif opc == SACERDOTISA:
        print('''
        Fuerza: 18
        Energia: 25
        Especial: 22
        ''')
    elif opc == SALIR:
        continuar = False
    else:
        print('Opcion no valida')
    input('Presiona enter para continuar...')
input('Nos vemos...')