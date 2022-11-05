'''
Secuencial_4.py
script en Python que solicite al usuario dos numeros 
y posteriormente muestre la suma de ambos valores
'''

valor_1 = input('Ingresa un numero: ')
#conversion del tipo str a int
valor_1 = int(valor_1)
valor_2 = int(input('Ingresa otro numero: '))

suma = valor_1 + valor_2
print(f'{valor_1} + {valor_2} = {suma}')