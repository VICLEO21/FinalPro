import pandas as pd


def printDicc(dicc):
    for i in dicc:
        print(f'Vertice: {i}')
        for j in dicc[i]:
            print(F'\tRel: {j} \n\t\tPeso: {dicc[i][j]}')
    return ''

nombre_archivo = input ('Nombre archivo: ')

df = pd.read_excel(nombre_archivo, index_col=0,)
    # Convierte el DataFrame a un diccionario de diccionarios
arr = df.to_dict(orient='index')
    # Elimina las claves de índice para que sean solo cadenas
arr = {str(k): v for k, v in arr.items()}


def dijkstra(graph, start, nodes):
    # Inicialización de distancias, nodos visitados y recorridos
    distancias = {node: None for node in nodes}
    distancias[start] = 0
    visited = {node: False for node in nodes}
    paths = {node: [start] for node in nodes}
    nodos_Visitados = []
    
    # Bucle principal
    for i in range(len(nodes)):
        # Encuentra el nodo con la distancia mínima no visitada
        dist = None
        nodoMin = None
        for node in nodes:
            if not visited[node] and (dist is None or (distancias[node] is not None and distancias[node] < dist)):
                dist = distancias[node]
                nodoMin = node
        
        # Marca el nodo como visitado
        visited[nodoMin] = True
        nodos_Visitados.append(nodoMin)
        
        # Actualiza las distancias y los recorridos a los nodos adyacentes
        for node in nodes:
            if not visited[node] and graph[nodoMin][node] != 0:
                new_dist = distancias[nodoMin] + graph[nodoMin][node]
                if distancias[node] is None or new_dist < distancias[node]:
                    distancias[node] = new_dist
                    paths[node] = paths[nodoMin] + [node]
    
    # Convierte los nodos en el camino más corto a etiquetas de vértices
    etiquetas = {node: [vertices[j] for j in path] for node, path in paths.items()}
    
    return distancias, etiquetas, nodos_Visitados

nodos = list(arr.keys())
aristas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
vertices = dict(zip(nodos, aristas))