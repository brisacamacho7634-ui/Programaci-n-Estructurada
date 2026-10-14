import csv


def contenido_csv(nombre_archivo):
    with open(
        nombre_archivo, mode="r", newline="", encoding="utf-8"
    ) as archivo:
        lector = csv.reader(archivo)

        columnas = [col.strip() for col in next(lector)]
        print("Columnas:", columnas)

        filas = list(lector)

        nombre_index = columnas.index("nombre")

        for i in range(len(filas)):
            for j in range(len(filas) - 1 - i):
                if (
                    filas[j][nombre_index].lower()
                    > filas[j + 1][nombre_index].lower()
                ):
                    filas[j], filas[j + 1] = filas[j + 1], filas[j]
        for fila in filas:
            print("Nombre:", fila[nombre_index])

        with open(
            "pacientes_ordenados.csv", mode="w", newline="", encoding="utf-8"
        ) as archivo_salida:
            escritor = csv.writer(archivo_salida)
            escritor.writerow(columnas)
            escritor.writerows(filas)

        print("Archivo ordenado creado correctamente.")
        return columnas, filas


if __name__ == "__main__":
    nombre_archivo = "pacientes_mini - pacientes_mini.csv"
    columnas, filas = contenido_csv(nombre_archivo)