import csv

def contenido_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)

        # Imprimir las columnas del archivo CSV
        archivo.seek(0)  # Reset file pointer to the beginning
        columnas = next(lector)  # Get the first row (column names)
        print("Columnas:", columnas)

        # Listar el contenido de la columna "Nombre"
        nombre_index = columnas.index("nombre")
        archivo.seek(0)  # Reset file pointer to the beginning
        next(lector)  # Skip the header row
        for fila in lector:
            print("Nombre:", fila[nombre_index])


if __name__ == "__main__":
    nombre_archivo = r"pacientes.csv"

    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        
        # Imprimir las columnas del archivo CSV
        archivo.seek(0)  # Reset file pointer to the beginning
        columnas = next(lector)  # Get the first row (column names)
        print("Columnas:", columnas)

        # Listar el contenido de la columna "Nombre"
        nombre_index = columnas.index("nombre")
        archivo.seek(0)  # Reset file pointer to the beginning
        next(lector)  # Skip the header row
        for fila in lector:
            print("Nombre:", fila[nombre_index])

def ordenar_por_id_y_guardar_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        
        # 1. Leer encabezado y filas
        encabezado = next(lector)
        filas = list(lector)
        
        # Obtener el índice de la columna "id"
        id_index = encabezado.index("id")

    # 2. Ordenar las filas por la columna "id" numéricamente de forma ascendente
    filas_ordenadas = sorted(filas, key=lambda x: int(x[id_index]))

    # 3. Escribir el nuevo archivo CSV con el contenido ordenado
    with open(archivo_salida, mode='w', newline='', encoding='utf-8') as archivo_nuevo:
        escritor = csv.writer(archivo_nuevo)
        
        # Escribir el encabezado
        escritor.writerow(encabezado)
        
        # Escribir las filas ya ordenadas
        escritor.writerows(filas_ordenadas)

    print(f"¡Archivo '{archivo_salida}' ordenado por ID generado exitosamente!")


if __name__ == "__main__":
    nombre_archivo_entrada = "pacientes.csv"
    nombre_archivo_salida = "pacientes_ordenados_por_id.csv"
    
    ordenar_por_id_y_guardar_csv(nombre_archivo_entrada, nombre_archivo_salida)