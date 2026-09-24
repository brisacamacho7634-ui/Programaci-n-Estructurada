MAX_INTENTOS = 3
def verificar_pin():
    while True:
        try:
            pin_correcto = int(input("PIN correcto: "))
            break
        except ValueError:
            print("Escribe un numero entero.")
    intentos = 0
    acerto = False
    while intentos < MAX_INTENTOS and not acerto:
        try:
            pin_teclado = int(input(f"PIN (intento {intentos + 1}): "))

            if pin_teclado == pin_correcto:
                acerto = True
            intentos += 1

        except ValueError:
            print("Escribe un numero entero.")
    if acerto:
        mensaje = "ACCESO"
    else:
        mensaje = "DENEGADO"
    print(mensaje)


if __name__ == "__main__":
    verificar_pin()