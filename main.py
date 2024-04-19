import pandas as pd
import openpyxl
from lib import *



df = pd.read_excel(nombre_archivo,sheet_name='Hoja1',engine='openpyxl')
array = df.values

print("")
print("Matriz de Adyacencia: ")
print (array)
print("")

vertices = df.columns.tolist()
aristas = []

for i in range(df.shape[0]):
    origen = df.index[i]
    for j in range(df.shape[1]):
        destino = df.columns[j]
        peso = df.iloc[i, j]
        if pd.notna(peso) and peso != 0:
            aristas.append((origen, destino, peso))

            
cadena = ""
for arista in aristas:
    cadena += f"[{arista[0]}] -> [{arista[1]}] : Peso [{arista[2]}], "

print("Lista de relación: ")
print(cadena[:-2]) 
print ("")

df = pd.read_excel(nombre_archivo, index_col=0,)
    # Hacer diccionarios
arr = df.to_dict(orient='index')
arr = {str(k): v for k, v in arr.items()}



nodos = list(arr.keys())


aristas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# etiquetas de los vértices
vertices = dict(zip(nodos, aristas))

inicio = 'B'
fin = 'H'
caminoCorto, paths, nodos_Visitados = dijkstra(arr, inicio, nodos)
print("")
print("Path: ")
print("")

print("Cola: ")
print("")

print("Visitados:", "','".join([vertices[node] for node in nodos_Visitados]))
print("")

print("Recorrido:", "','".join(paths[fin]))
print("")

print(f"Peso Total: {caminoCorto[fin]}")
print("")