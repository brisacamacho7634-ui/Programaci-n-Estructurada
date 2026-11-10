import pandas as pd
df = pd.read_csv("pacientes - pacientes.csv")
#EJERCICIO 4
import pandas as pd
df = pd.read_csv("pacientes - pacientes.csv")
#a) ¿Cuantos pacientes y cuantas columnas hay?
print("Dimensiones(filas, columnas):" , df.shape)
print(f"   Hay {df.shape[0]} pacientes y {df.shape[1]} columnas.")
#b) ¿Que columnas tienen faltantes y cuantos?
faltantes = df.isna().sum()
print("/nb) columnas con valores faltantes:")
print(faltantes[faltantes > 0])
#c) ¿Que tipo de dato tiene cada columna?
print("tipos de datos de cada columna:")
print(df.dtypes)


#EJERCICIO 5
#Filtrar pacientes con fiebre y taquicardia
alerta = df[(df["temp_c"] >= 38) & (df["fc_lpm"] > 100)]
#para a y b
print("pacientes en alerta")
print(f"¿Cuantos son?: {len(alerta)}")
print("\nDatos solicitados (id, temp_c, fc_lpm, servicio):")
print(alerta[["id", "temp_c", "fc_lpm", "servicio"]])
#para c
print("¿En que servicios estan?")
print(alerta["servicio"].value_counts())


#EJERCICIO 6
#a)crear la columna imc
df["imc"] = df["peso_kg"] / (df["estatura_m"] ** 2)
#b)clasificala: <18.5 bajo peso, 18.5 - 24.9 normal, 25 - 29.9 sobrepeso,>= 30 obesidad
bins = [0, 18.5, 25, 30, 100]
labels = ["bajo peso", "normal", "sobrepeso", "obesidad"]
df["imc_cat"] = pd.cut(df["imc"], bins = bins, labels = labels, right = False)
#c)cuenta pacirentes por categorias, ¿Cuantos quedaron sin imc y por que?
print("conteo por categoria de imc")
print(df["imc_cat"].value_counts(dropna = False))
print("\n¿cuantos quedaron sin IMC y por que?")
nans_imc = df["imc_cat"].isna().sum()
print(f"quedaron {nans_imc} pacientes sin imc por no tener registrado de su peso (peso_kg es NaN).")


# EJERCICIO 7
resumen = (
    df.groupby("servicio")
    .agg(
        num_pacientes=("id", "count"),
        temp_promedio=("temp_c", "mean"),
        fc_promedio=("fc_lpm", "mean")
    )
    .round(1)
    .sort_values("fc_promedio", ascending=False)
)
print("resumen por servicio")
print(resumen)