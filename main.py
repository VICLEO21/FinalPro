import pandas as pd
import openpyxl
from lib import *
import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

#-----------------------------------------------------------------------------

nombre_archivo = input("Nombre del archivo: ")

df = pd.read_excel(nombre_archivo,sheet_name='Sheet',engine='openpyxl')
array = df.values


globalArrayNum = []
def contadorDos(inicio,fin):
    logging.info(f'Funcion con rango: {inicio} - {fin}')
    for i in range (inicio,fin+1,1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

subrango = 200//4
rangoActual = 1
executors = 4

with ThreadPoolExecutor(max_workers=2) as executor:
    for i in range (1,executors +1,1):
        j = subrango * i
        executor.submit(contadorDos, rangoActual , j)
        rangoActual = subrango + rangoActual


sumatoria = 0
for fila in array:
    for elemento in fila:
        sumatoria += elemento
            
            
print (sumatoria)            
    