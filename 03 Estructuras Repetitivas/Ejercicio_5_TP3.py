# Ejercicio N° 5 - Scape Room - La Arena del Gladiador
# Alumna: Lilian Ruth Ismach


# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_jugador = True 

# Mensaje de bienvenida
print("===== BIENVENIDO A LA ARENA =====")

# Nombre del gladiador
nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo se permiten letras. Vuelva a intentarlo.")
    nombre = input("Nombre del Gladiador: ").strip()


print("===== INICIO DEL COMBATE =====")

# Bucle principal
while vida_jugador > 0 and vida_enemigo > 0:
    
    # Estado de los jugadores
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    # Menú del jugador
    if turno_jugador:
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        opcion = input("Opción: ")

        # Validación de la opción ingresada
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")
        opcion = int(opcion)

        # ----------------- ATAQUE PESADO ----------------------------------
        if opcion == 1:
            if vida_enemigo < 20:
                danio = danio_base * 1.5
            else:
                danio = danio_base

            vida_enemigo -= danio
            print(f"Atacaste al enemigo por {danio:.2f} puntos de daño!")

        # ----------------- RAFAGA VELOZ ----------------------------------        
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for contador in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # ----------------- CURAR ----------------------------------
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Recuperaste 30 puntos de vida.")
            else:
                print("No quedan pociones!")
        turno_jugador = False 

    else:
        # Ataque automático del enemigo.
        print(">> Turno del enemigo")
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")
        turno_jugador = True    


if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")