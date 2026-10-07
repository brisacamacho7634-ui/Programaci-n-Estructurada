import time
#Fuerza Bruta
def suma_objetivo_conjunto1(Lista, objetivo):
    n = len(Lista)
    for i in range(n):
        for j in range(i + 1, n):
            if Lista[i] + Lista[j] == objetivo:
                return True
    return False
#Con set/conjunto
def suma_objetivo_conjunto2(Lista, objetivo):
    vistos = set()
    for numero in Lista:
        complemento = objetivo - numero
        if complemento in vistos:
            return True
        vistos.add(numero)
    return False
#reto: mide y muestra tiempos
tamaños = [1000, 2000, 4000, 8000]
print("n\t| Tiempo V1 (Fuerza Bruta)\t| Tiempo V2 (Conjunto)")
print("-" * 60)

for n in tamaños:
    # Genera lista básica sin librerías externas
    Lista = list(range(n))
    objetivo_imposible = -1  # Peor caso

    # Medición Versión 1
    inicio1 = time.perf_counter()
    suma_objetivo_conjunto1(Lista, objetivo_imposible)
    fin1 = time.perf_counter()
    tiempo1 = fin1 - inicio1

    # Medición Versión 2
    inicio2 = time.perf_counter()
    suma_objetivo_conjunto2(Lista, objetivo_imposible)
    fin2 = time.perf_counter()
    tiempo2 = fin2 - inicio2

    # Imprimir en consola
    print(f"{n}\t| {tiempo1:.6f} s\t\t\t| {tiempo2:.6f} s")
