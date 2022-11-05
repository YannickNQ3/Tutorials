'''
anidamiento_estructural.py
script en Python que simula un juego de preguntas y respuestas,
si el usuario contesta correctamente una pregunta puede continuar
con la siguiente, en caso de fallar se le indica que ha perdido.
Si contesta acertadamente todas las preguntas se le felicita por
su conocimiento.
'''
print('Bienvenid@ pongamos a prueba tu conocimiento :V')
respuesta = int(input('¿Cuál es la velocidad de la luz en m/s?'))
if respuesta == 299792458:
    print('¡Correcto!')
    respuesta = int(input('¿Cuanto es 8+8/8*8?'))
    if respuesta == 8+8/8*8:
        print('Correcto')
        respuesta = input('¿De que color eran las mangas del chaleco de Cristobal Colon?')
        if respuesta == 'Los chalecos no tienen mangas':
            print('Felicidades te has llevado un millón de pesos')
        else:
            print('Lo siento, respuesta incorrecta')
    else:
        print('Lo siento, respuesta incorrecta')
else:
    print('Lo siento, respuesta incorrecta')
print('Nos vemos')