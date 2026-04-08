# Ejercicio N° 4 - Scape Room - Bóveda
# Alumna: Lilian Ruth Ismach

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzadas = 0
# Separador visual para la consola
separador = "-----------------------------------------------------------------"

print(separador)
print("Scape Room - La Bóveda")
print(separador)

# Nombre del agente
nombre = input("Nombre del agente: ").strip()
while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Nombre del agente: ").strip()

print(f"Bienvenido/a {nombre}")
# Bucle principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print(separador)
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")
    print(separador)
    print("MENÚ DE OPCIONES:")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    print(separador)

    opcion = input("Opción: ")
    # Validación de la opción
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error. La opción ingresada no es válida. Vuelva a intentar.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    # ---------------------- OPCIÓN 1: FORZAR ---------------
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzadas += 1

        print(">>>>> Forzando cerradura...")              
        # Regla Antispam
        if forzadas == 3:
            alarma = True
            print("La cerradura se trabó. Alarma activada!.")
        else:
            # Riesgo de alarma por energía baja
            if energia < 40:
                print("Riesgo de alarma!!.")
                num = input("Elilja un número (1-3): ")
                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    print("Error. El número elegido no es válido. Vuelva a intentar.")
                    num = input("Elilja un número (1-3): ")

                if int(num) == 3:
                    alarma = True
                    print("Falló. Se activó la alarma!!")

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura abierta!!")
            
    # ---------------------- OPCIÓN 2: HACKEAR PANEL------------------
    
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzadas = 0

        print(">>>>> Hackeando Panel...")
        for contador in range(4):
            codigo_parcial += "A"
            print(f"...{codigo_parcial}")
           

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo finalizado! Cerradura abierta.")

    # ---------------------- OPCIÓN 3: DESCANSAR -------------------
    elif opcion == 3:
        energia += 15
        tiempo -= 1
        forzadas = 0

        print(">>>>> Descansando para recuperar recursos...")
        # Límite de energía
        if energia > 100:
            energia = 100
            print("Ha alcanzado el nivel máximo de energía!")

        if alarma:
            energia -= 10
            print("Se restaron 10 puntos de energía extra por alarma activa!")


    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        break


print(separador)
print("Juego Finalizado - Resultado Obtenido:")
if cerraduras_abiertas == 3:
    print("VICTORIA: Ha logrado abrir la bóveda!!")
elif energia <= 0 or tiempo <= 0:
    print(f"DERROTA: Se agotaron los recursos antes de abrir la bóveda.")
else:
    print(f"DERROTA: Sistema bloqueado por alarma.")
print(separador)
