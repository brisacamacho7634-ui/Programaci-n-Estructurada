#EJERCICIO 1
import numpy as np
sistolica = np.array(
    [118, 135, 142, 110, 128, 155, 121]
)

#a) Calcula el promedio y la desviacion estandar
promedio = np.mean(sistolica)
desv_est = np.std(sistolica)
print("promedio:", promedio)
print("desviacion estadar:", desv_est)
#b) Cuebnta cuantas lescturas son >= 130 mmHg
mayores_130 = sistolica >= 130
cantidad = np.sum(mayores_130)
print("Lecturas >= 130:", cantidad)
#c) Indica en que posiciones estam estas lecturas
posiciones = np.flatnonzero(sistolica >= 130)
print("posiciones:", posiciones)


#EJERCICIO 2
glucosa = np.array([
    [ 95, 102,  99],
    [140, 155, 148],
    [ 88,  91,  85],
    [110, 118, 125],
    ])
#a) Promedio de glucosa por paciente
promedio_paciente = np.mean(glucosa, axis=1)
print("promedio por paciente:", promedio_paciente)
#b) Promedio por dia: ¿que dia fue el mas alto?
promedio_dia = np.mean(glucosa, axis=0)
dia_mas_alto = np.argmax(promedio_dia)
print("promedio por dia:", promedio_dia)
print("el dia con el promedio mas alto:", dia_mas_alto)
#c) ¿Que paciente y que dia tuvieron el valor maximo?
max_val = np.max(glucosa)
paciente_idx, dia_idx = np.unravel_index(np.argmax(glucosa), glucosa.shape)
print("valor maximo:", max_val)
print("paciente (fila):", paciente_idx, "dia (columna):", dia_idx)


#EJERCICIO 3
datos = np.array([
    [36.5,  72,  95],
    [38.2, 104, 140],
    [37.0,  80,  88],
    [36.8,  65, 110],
    [39.1, 112, 125],
    ])
#a) y b) Escala cada columna al rango [0, 1] sin usar ciclos
min_col = np.min(datos, axis=0)
max_col = np.max(datos, axis=0)
datos_normalizados = (datos - min_col) / (max_col - min_col)
print("datos normalizados:\n", datos_normalizados)
#c) Verifica que cada columna tenga minimo 0 y maximo 1
print("minimo por columna:", np.min(datos_normalizados, axis=0))
print("maximo por columna:", np.max(datos_normalizados,axis=0))
