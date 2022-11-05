'''
funciones_5.py
script en Python que implemente una función que haga el calculo del
IMC del usuario. La función debe recibir el peso y la alturaa del
usuario y como resultado regresa el valor de índice de masa corporal.
'''

def calcular_IMC(peso, estatura):
    return peso /(estatura**2)

print('Vamos a calcular tu IMC')
print('Ingresa los sisguientes datos')
peso = float(input('Peso: '))
estatura = float(input('Estatura: '))

print(f'Tu índice de masa corporal es: {calcular_IMC(peso, estatura) :.2f}')

print('Nos vemos')