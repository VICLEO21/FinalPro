import pandas as pd
import openpyxl
from lib import *
import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor
import os

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

#-----------------------------------------------------------------------------
#Nombre archivo dinamico
nombre_archivo = input("Nombre del archivo: ")

#Lectura de archivo guardando en array
df = pd.read_excel(nombre_archivo,sheet_name='Sheet',engine='openpyxl')
array = df.values

#Número de hilos a usar dinamico 
num_Hilos = 0 
while num_Hilos <2 or num_Hilos>9:
    os.system ("cls")
    num_Hilos = int(input ("Número de hilos a usar: "))




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

with ThreadPoolExecutor(max_workers =  num_Hilos ) as executor:
    for i in range (1,executors +1,1):
        j = subrango * i
        executor.submit(contadorDos, rangoActual , j)
        rangoActual = subrango + rangoActual





def suma (arr):
    sumaTotal = 0 
    for fila in arr:
        sumaFila = sum(fila)
        sumaTotal += sumaFila
    return sumaTotal



print (suma (array))
    

            
