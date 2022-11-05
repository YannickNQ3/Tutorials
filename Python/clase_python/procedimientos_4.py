'''
procedimientos_4.py
Script en Python que muestre un menú ciclico; dicho menú sera 
implementado en un procedimiento
'''
import os
ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4
def mostrar_menu():
    print(f'''
    {ESP}) Español
    {ING}) Ingles
    {NO_SUBS}) Sin subtitulos
    {SALIR}) Salir
    ''')

continuar = True
while continuar:
    os.system('cls')
    mostrar_menu()
    opc = int(input('Selecciona una opción: '))
    os.system('cls')
    if opc == ESP:
        print('Subtitulos en español')
    elif opc == ING:
        print('Subtitulos en Ingles')
    elif opc == NO_SUBS:
        print('Subtitulos apagados')
    elif opc == SALIR:
        continuar = False
    else:
        print('Opción no válida')
    input('Presiona enter para continuar...')
print('Nos vemos...')