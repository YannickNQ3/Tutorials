'''
selectiva_simple_4.py
script en Python que pregunte al usuario cuanto
indica el termómetro y si ese valor se encuetra 
entre 18 y 27 que le indique que la temperatura
es agradable
'''

temperatura = int(input('¿Cuánto indica el termómentro? '))

if 18 <= temperatura <= 27:
    print('El clima está agradable')
print('Nos vemos pronto!')
