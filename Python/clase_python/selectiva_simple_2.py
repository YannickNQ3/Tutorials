'''
Selectiva_simple_2.py
script en Python que genere un numero aleatorio
entre 1 y 50 y le pda al usuario que intente
adivinarlo. Si adivina el número que lo 
felicite por su logro
'''

#Agrega el modulo random a mi programa y 
#con ello me permite generar numeros aleatorios

import random

secreto = random.randint(1, 10)

print('Acabo de generar un número aleatorio entre 1 y 10. Intenta adivinarlo')

numero = int(input('¿Cuál crees que sea mi numero?'))

if numero == secreto:
    print('Logro desbloqueado: Adivin@ Mistic@')
print('Sigue disfrutando tu día')
print(f'El numero secreto es {secreto}')