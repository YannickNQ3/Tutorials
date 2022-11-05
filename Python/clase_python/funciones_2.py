'''
funciones_2.py
script en Python que implemente una función encargada de calcular
el índice de masa corporal del usuario.
'''
def calcular_IMC():
    peso = float(input('Peso: '))
    estatura = float(input('Estatura: '))
    imc = peso /(estatura**2)
    return imc

print('Vamos a calcular tu IMC')
imc = calcular_IMC()

print(f'Tu índice de masa corporal es: {imc :.2f}')

print('Nos vemos')