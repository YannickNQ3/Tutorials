'''
selectiva_doble_2.py
script en Python que simule un sistema de validación
de una plataforma digital. El usuario deberá 
proporcionar tanto su nombre como la contraseña.
Si los valores coinciden con los previamente almacenados
entonces se le dará la bienvenida, sino se le indicará que hubo 
un error.
'''

USER = 'Pep3'
PASSWORD = 'Nava123'

print('Proporciona los siguientes datos: ')

user = input('Usuario: ')
password = input('Contraseña: ')

if user == USER and password == PASSWORD:
    print('             insta [°]')
    print('Bienvenid@ a tu cuenta')
else:
    print('Datos incorrectos, intenta de nuevo.')
print('Que tengas un buen día')