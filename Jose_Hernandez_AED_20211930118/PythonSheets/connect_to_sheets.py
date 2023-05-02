import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)

client = gspread.authorize(creds)

sheet = client.open('PythonSheets').sheet1

# access data 
# print(sheet.get_all_records()) #get all records from a table
# print(sheet.row_values(1)) #get all values from a row
# print(sheet.col_values(1)) #get all values from a column
# print(sheet.cell_(1,3).value) #get value from a specific cell

#arr = [sheet.cell(1,1).value,sheet.cell(2,1).value,sheet.cell(3,1).value,sheet.cell(4,1).value,sheet.cell(5,1).value,sheet.cell(6,1).value,sheet.cell(7,1).value,sheet.cell(8,1).value,sheet.cell(9,1).value,sheet.cell(10,1).value,sheet.cell(10,1).value,sheet.cell(11,1).value]
#print (arr)
#print(type(sheet.cell(10,1).value))
#arr_int = int()

#insert data
#sheet.insert_row(["MI","PRIMER","HOLA","MUNDO",2])

#delete data
#sheet.delete_row(3)

#update cell
#sheet.update_cell(3,1,"45")

#find specific value
#cell = sheet.find("72")
#print(cell.value)
#print(cell.row)
#print(cell.col)

#Numeros Aleatorios
# Generar una lista de 10 números aleatorios entre 1 y 100 (inclusivo)
numsrand = [random.randint(1, 100) for _ in range(10)]

# Escriba los números aleatorios en las celdas de la columna A de A2 a A11
listog = sheet.range('A2:A11')
for i in range(len(listog)):
    listog[i].value = str(numsrand[i])

# Actualizar los valores en la hoja
sheet.update_cells(listog)

#Bubble
# definir el rango de celdas a ordenar
sortrange = 'A2:A11'

# Recuperar los datos de las celdas
data = sheet.range(sortrange)

# Realizar bubble sort hasta que todos los números se ordenan en orden ascendente
n = len(data)
while True:
    swapped = False
    for i in range(n - 1):
        if float(data[i].value) > float(data[i + 1].value):
            data[i], data[i + 1] = data[i + 1], data[i]
            swapped = True

            # Mostrar el progreso de clasificación en las celdas de la columna C de C2 a C11
            progreso_sorting = [cell.value for cell in data]
            sheet.update('C2:C11', [[value] for value in progreso_sorting])

    # Si no se intercambiaron números, la lista está ordenada y se sale del bucle
    if not swapped:
        break

# Escribir los datos ordenados en las celdas de la columna C de C2 a C11
valores_surteados = [cell.value for cell in data]
sheet.update('C2:C11', [[value] for value in valores_surteados])

#Selection
# Definir el rango de celdas a ordenar
sortrange = 'A2:A11'

# Recuperar los datos de las celdas
data = sheet.range(sortrange)

# Realizar Selection Sort hasta que todos los números estén ordenados en orden ascendente
n = len(data)
for i in range(n - 1):
    minindx = i
    for j in range(i + 1, n):
        if float(data[j].value) < float(data[minindx].value):
            minindx = j

    # Intercambiar el valor mínimo con el valor actual si es necesario
    if minindx != i:
        data[i], data[minindx] = data[minindx], data[i]

    # Mostrar el progreso de clasificación en las celdas de la columna D de D2 a D11
    progreso_sorting = [cell.value for cell in data]
    sheet.update('D2:D11', [[value] for value in progreso_sorting])

# Escribir los datos ordenados en las celdas de la columna D de D2 a D11
valores_surteados = [cell.value for cell in data]
sheet.update('D2:D11', [[value] for value in valores_surteados])

#Insertion
# definir el rango de celdas a ordenar
sortrange = 'A2:A11'

# Recuperar los datos de las celdas
data = sheet.range(sortrange)

# Realizar Insertion Sort hasta que todos los números estén ordenados en orden ascendente
n = len(data)
for i in range(1, n):
    valor_act = float(data[i].value)
    j = i - 1
    while j >= 0 and float(data[j].value) > valor_act:
        data[j + 1].value = data[j].value
        j -= 1

    data[j + 1].value = str(valor_act)

    # Mostrar el progreso de clasificación en las celdas de la columna E de E2 a E11
    progreso_sorting = [cell.value for cell in data]
    sheet.update('E2:E11', [[value] for value in progreso_sorting])

# Escriba los datos ordenados en las celdas de la columna E de E2 a E11
valores_surteados = [cell.value for cell in data]
sheet.update('E2:E11', [[value] for value in valores_surteados])
