import pandas as pd
import openpyxl

#nombre_archivo = input ('Nombre archivo: ')

#wb = openpyxl.load_workbook(nombre_archivo)
#hoja = wb.active
#filas = hoja.max_row
#columnas = hoja.max_column

#array=[]
#for fila in range (1, filas + 1):
#    fila_Numeros = []
#    for columna in range (1, columnas +1):
#        valor_celda = hoja.cell(row=fila, column=columna).value
#        array.append(valor_celda)

#print(array)

df = pd.read_excel('datos-Eval-3.xlsx',sheet_name='Hoja1',index_col=0,engine='openpyxl')
array = df.values

print (array)





#def printDicc(dicc):
#    for i in dicc:
#        print(f'Vertice: {i}')
#        for j in dicc[i]:
#            print(f'\tDestino: {j} \t\tPeso: {dicc[i][j]}')
#    return ''


#df = pd.read_excel(nombre_archivo,index_col=0, engine='openpyxl')

#vertices = df.columns.tolist()


#printDicc()