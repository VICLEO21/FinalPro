import pandas as pd
import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor
import os 

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")



nombre_archivo = input("Nombre del archivo: ")

df = pd.read_excel(nombre_archivo,sheet_name='Sheet',engine='openpyxl')
array = df.values

numHilos = 0 
while numHilos <2 or numHilos>10:
    os.system ("cls")
    numHilos = int(input ("Número de hilos a usar entre 2 a 10: "))
    print("")


def sumaHilo(datos, inicio, fin):
    sumaParcial = suma(datos[inicio:fin])
    print(f"Suma de hilo: {sumaParcial}")


def suma (array):
    sumaTotal = 0 
    for fila in array:
        sumaFila = 0 
        for elemento in fila:
            sumaFila += elemento
        sumaTotal += sumaFila
    return sumaTotal


datos = len(array)
hilo = datos // numHilos

t0 = time.time()
hilos = []
inicio = 0

for i in range(numHilos):
    fin = inicio + datos//numHilos 
    hilo = threading.Thread(target=sumaHilo, args=(array, inicio, fin))
    hilos.append(hilo)
    inicio = fin
    hilo.start()

for hilo in hilos:
    hilo.join()
tf=time.time()-t0



print ("")
print(f'Tiempo de ejecucion: {tf}')
print ("")
print(f"Suma Total: {suma(array)}")
    
    
            
