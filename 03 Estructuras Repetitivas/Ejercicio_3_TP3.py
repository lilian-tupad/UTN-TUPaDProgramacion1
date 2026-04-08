# Ejercicio N° 3 - Agenda de Turnos
# Alumna: Lilian Ruth Ismach

# Variables que representan los turnos disponibles (vacío = libre)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Separador visual para la consola
separador = "-----------------------------------------------------------------"

# Nombre del programa
print(separador)
print("Agenda de turnos")
print(separador)

# Validación del nombre del operador (solo letras)
operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Ingrese solo letras.")
    operador = input("Nombre del operador: ").strip()
print(f"Bienvenido/a {operador}")

opcion_menu = 0

# Bucle principal del programa (se repite hasta elegir salir)
while opcion_menu != 5:
    print(separador)
    print("MENU DE OPCIONES:")
    print(separador)
    print("1) Reservar Turno")
    print("2) Cancelar Turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    print(separador)

    opcion_menu = input("Ingrese una opción: ")

    # Validación de opción de menú
    while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 5:
        print("Opción no válida.")
        opcion_menu = input("Ingrese una opción: ")

    opcion_menu = int(opcion_menu)

    # ---------------- RESERVAR ----------------
    if opcion_menu == 1:
        print(separador)
        print(">>>>> Reservar Turno:")
        
        # Elección y validación del día
        dia = input("Seleccione el día: 1 (Lunes) o 2 (Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Valor no válido.")
            dia = input("Seleccione el día: 1 (Lunes) o 2 (Martes): ")
        dia = int(dia)

        # Ingreso y validación del nombre del paciente
        paciente = input("Nombre del Paciente: ").strip()
        while not paciente.isalpha():
            print("Ingrese solo letras.")
            paciente = input("Nombre del Paciente: ").strip()

        # Variables auxiliares para controlar el resultado
        dia_turno_str = "Lunes" if dia == 1 else "Martes"
        estado_reserva = "reservado"
         
        if dia == 1:
            # Verifico si el paciente ya tiene turno
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                estado_reserva = "repetido" 
            # Asigno el primer turno libre disponible
            elif lunes1 == "":
                lunes1 = paciente            
            elif lunes2 == "":
                lunes2 = paciente
            elif lunes3 == "":
                lunes3 = paciente
            elif lunes4 == "":
                lunes4 = paciente
            else:
                # No hay turnos disponibles
                estado_reserva = "completo"
        else:
            # Verifico si el paciente ya tiene turno
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                estado_reserva = "repetido"
            # Asigno el primer turno libre disponible
            elif martes1 == "":
                martes1 = paciente
            elif martes2 == "":
                martes2 = paciente
            elif martes3 == "":
                martes3 = paciente
            else:
                # No hay turnos disponibles
                estado_reserva = "completo"
        
        # Mensajes finales según el resultado
        if estado_reserva == "reservado":
            print(">>>>> Turno reservado correctamente.")
        elif estado_reserva == "repetido":
            print(f">>> El paciente ya tiene un turno reservado el día {dia_turno_str}")
        else:
            print(f">>> No hay turnos disponibles para el día {dia_turno_str}")

    # ---------------- CANCELAR ----------------
    elif opcion_menu == 2:
        print(separador)
        print(">>>>> Cancelar Turno:")

        # Selección y validación del día
        dia = input("Seleccione el día: 1 (Lunes) o 2 (Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Valor no válido.")
            dia = input("Seleccione el día: 1 (Lunes) o 2 (Martes): ")
        dia = int(dia)

        # Ingreso del paciente
        paciente = input("Nombre del Paciente: ").strip()
        while not paciente.isalpha():
            print("Ingrese solo letras.")
            paciente = input("Nombre del Paciente: ").strip()

        dia_turno_str = "Lunes" if dia != 2 else "Martes"
        cancelado = False

        # Búsqueda y cancelación del turno
        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        # Resultado de la operación
        if cancelado:
            print(">>>>> Turno cancelado correctamente.")
        else:
            print(f">>>>> No se encontró el turno del paciente: {paciente} para el día {dia_turno_str}.")

    # ---------------- VER AGENDA ----------------
    elif opcion_menu == 3:
        # Selección y validación del día
        dia = input("Seleccione el día: 1 (Lunes) o 2 (Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Valor no válido.")
            dia = input("Seleccione el día: 1 (Lunes) o 2 (Martes): ")
        dia = int(dia)

        print(separador)

        # Mostrar agenda del día seleccionado
        if dia == 1:
            print(">>>>> Agenda Lunes:")
            print(separador)
            print("Turno 1:", lunes1 if lunes1 != "" else "Libre")
            print("Turno 2:", lunes2 if lunes2 != "" else "Libre")
            print("Turno 3:", lunes3 if lunes3 != "" else "Libre")
            print("Turno 4:", lunes4 if lunes4 != "" else "Libre")
        else:
            print(">>>>> Agenda Martes:")
            print(separador)
            print("Turno 1:", martes1 if martes1 != "" else "Libre")
            print("Turno 2:", martes2 if martes2 != "" else "Libre")
            print("Turno 3:", martes3 if martes3 != "" else "Libre")

    # ---------------- RESUMEN ----------------
    elif opcion_menu == 4:
        # Conteo de turnos ocupados
        turnos_lunes = 0
        if lunes1 != "": turnos_lunes += 1
        if lunes2 != "": turnos_lunes += 1
        if lunes3 != "": turnos_lunes += 1
        if lunes4 != "": turnos_lunes += 1

        turnos_martes = 0
        if martes1 != "": turnos_martes += 1
        if martes2 != "": turnos_martes += 1
        if martes3 != "": turnos_martes += 1

        # Determinar el día con mayor cantidad de turnos
        if turnos_lunes > turnos_martes:
            mayor = "Lunes"
        elif turnos_martes > turnos_lunes:
            mayor = "Martes"
        else:
            mayor = "Empate"

        print(separador)
        print(">>>>> Resumen General:")
        print(separador)
        print(f"Lunes: {turnos_lunes} ocupados / {4 - turnos_lunes} disponibles")
        print(f"Martes: {turnos_martes} ocupados / {3 - turnos_martes} disponibles")
        print(f"Día con más turnos: {mayor}")

    # ---------------- SALIR ----------------
    else:
        print(separador)
        print(">>>>> Cerrando el sistema...")
        print(separador)