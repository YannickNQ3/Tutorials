'''
Selectiva_simple_3.py
script en Python que solicite la calificación
y cantidad de asistencias a un curso. Si la
calificación es mayor o igual que 60 y la
cantidad de asistencias es mayor que 20
entonces que le indique que ha aprobado el
curso.
'''

calificación = int(input('¿Cuál es tu calificación? '))
asistencias = int(input('¿Cuántas asistencias tuviste? '))

if calificación >= 60 and asistencias >= 20:
    print('Felicidades aprobaste el curso')
    if calificación >= 95:
        print('Estudiante sobresaliente. Pidele beca a AMLO.')

print('Sigue disfrutando tu dia')

