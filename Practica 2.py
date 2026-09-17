#leer saldo, retirado hoy y monto a retirar
saldo = float(input("Ingrese su saldo actual: "))
retirado_hoy = float(input("Ingrese el monto ya retirado de hoy: "))
monto_a_retirar= float(input("Ingrese el monto a retirar: "))

#el monto es multiplo de 50?
if monto_a_retirar % 50 != 0 or monto_a_retirar <= 0:
    print("MONTO NO VALIDO")
    print(f"saldo: sin cambio ({saldo})")
#monto <= al saldo?
else:
    if monto_a_retirar > saldo:
        print("SALDO INSUFICIENTE")
        print(f"saldo: sin cambio ({saldo})")
    else:
        # retirado hoy + monto <= 6000
        if retirado_hoy + monto_a_retirar > 6000:
            print("LIMITE DIARIO EXCEDIDO")
            print(f"saldo: sin cambio ({saldo})")
        else:
            # procesar el retiro
            saldo = saldo - monto_a_retirar
            print("ENTREGADO")
            print(f"saldo: nuevo {saldo}")







