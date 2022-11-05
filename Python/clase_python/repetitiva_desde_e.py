'''
repetitiva_desde_e.py
Script en Python que muestre un cronómetro en formato de 24 horas.
El despliegue seguirá el formato h:m:s. El cronometro deberá iniciar
en 0:0:0 y podrá llegar hasta 23:59:59. Implementar retardos de
1 segundo y limpieza de pantalla de forma tal que sólo se vea un tiempo
en pantalla
'''
import os
import time

for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            os.system('cls')
            print(f'{horas}: {minutos}: {segundos}')
            time.sleep(1)