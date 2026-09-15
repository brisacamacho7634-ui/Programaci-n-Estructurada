temp = float(input("Ingrese la temperatura (ºC): "))
fc = float(input("Ingrese la frecuencia cardiaca (fc): "))
sat = float(input("Ingrese la saturacion del oxigeno en la sangre (sat): "))
#####################
if sat < 90 or fc > 120:
    print("ROJO")
elif temp >= 39:
    print("AMARILLO")
else:
    print("VERDE")


