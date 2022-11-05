'''
selectiva_multiple_e.py
script en Python que simula una calculadora
con las operaciones aritmeticas básicas. El menú
será el siguiente:
1) Suma
2) Resta
3) Multiplicación
4) División
5) División Entera
6) Módulo
7) Potencia
'''

print('''       Operaciones Basicas
1) Suma
2) Resta
3) Multiplicación
4) División
5) División Entera
6) Módulo
7) Potencia
''')
opc = int(input('Selecciona una opción: '))
if 1<= opc <= 7:
    num_1= int(input('Ingrese un numero: '))
    num_2= int(input('Ingrese un numero: '))
    if opc == 1:
        sum= num_1 + num_2
        print(f'{num_1} + {num_2} es igual a {sum}')
    elif opc == 2:
        resta= num_1 - num_2
        print(f'{num_1} - {num_2} es igual a {resta}')
    elif opc == 3:
        prod= num_1 * num_2
        print(f'{num_1} X {num_2} es igual a {prod}')
    elif opc == 4:
        if num_2 != 0:
            coc= num_1 / num_2
            print(f'{num_1} / {num_2} es igual a {coc}')
        else:
            print('operacion no definida')
    elif opc == 5 and num_2 != 0:
        if num_2 != 0:
            cocE= num_1 // num_2
            print(f'Division Entera {num_1} / {num_2} es igual a {cocE}')
        else:
            print('operacion no definida')
    elif opc == 6 and num_2 != 0: 
        if num_2 != 0:
            mod= num_1 % num_2
            print(f'{num_1} % {num_2} es igual a {mod}')
        else:
            print('operacion no definida')
    elif opc == 7:
        pot= num_1 ** num_2
        print(f'{num_1} ^ {num_2} es igual a {pot}')
else:    
    print('Opción no válida')
print('Nos vemos!')