# Ejercicio N° 2 - Acceso al campus y Menú Seguro
# Alumna: Lilian Ruth Ismach

# credenciales fijas
nombre_usuario = "alumno"
clave_usuario = "python123"

# cantidad máxima de intentos
max_intentos = 3

# variables de control del bucle login
intento = 1
acceso_concedido = False

# Separador visual para la consola
separador = "-----------------------------------------------------------------"

# Nombre del programa
print(separador)
print("Acceso al Campus:")
print("Ingrese sus credenciales. Tiene hasta 3 intentos antes de que su cuenta se bloquee por seguridad.")
print(separador)

# Bucle para control del login del usuario
while intento <= max_intentos:
    usuario = input(f"Intento {intento}/{max_intentos} - Usuario: ").strip()
    clave = input("Clave: ")

    if usuario == nombre_usuario and clave == clave_usuario:
        acceso_concedido = True 
        break

    else:
        print("Error: Credenciales inválidas.")
        intento += 1

if not acceso_concedido:
    print(separador)
    print("Lo sentimo: Cuenta bloqueada")
    print(separador)

else:
    print(separador)
    print("Acceso concedido, bienvenio!")
    
    # Inicializo la variable para ingresar al menú
    opcion = 0
    
    while opcion != 4:
        print(separador)
        print("MENÚ DE OPCIONES:")
        print(separador)
        print("1) Estado.")
        print("2) Cambiar Clave.")
        print("3) Mensaje.")
        print("4) Salir.")
       
        # validación opción menú
        opcion = input("Ingrese una opción: ")
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            if opcion.isdigit():
                print("Error: valor fuera de rango. Vuelva a ingresar.")
            else:
                print("Error: ingrese un número válido. Vuelva a ingresar.")
            opcion = input("Ingrese una Opción: ")
        opcion = int(opcion)
        
        # ---------------- ESTADO ----------------
        if opcion == 1:
            print(separador)
            print("Estado de inscripción: Inscripto")
            print(separador)
        
        # ---------------- CAMBIO DE CLAVE ----------------   
        elif opcion == 2:            
            clave_modificada = False 
            while not clave_modificada:
                nueva_clave = input("Ingrese una nueva clave: ")
                
                # Validación de la longitud de la clave
                if len(nueva_clave) < 6:
                    print("Error: la nueva clave debe tener al menos 6 caracteres")
                    continue 
                
                # Validación de clave repetida (en uso)
                if nueva_clave == clave_usuario:
                    print("Error: La clave ingresada ya se encuentra en uso, por favor ingrese otra.")
                    continue
                
                # Confirmación de la clave
                reingreso_clave = input("Confirme la nueva clave: ")
                if reingreso_clave != nueva_clave:
                    print("Error: Las claves no coinciden. Vuelva a intentarlo.")
                    continue 

                # Actualización de la clave
                clave_usuario = nueva_clave
                clave_modificada = True                
                print(separador)
                print("La clave fue modificada con éxito!")
                print(separador)

        elif opcion == 3:
            print(separador)
            print("Muy bien....sigue así!")
            print(separador)

        else:
            print(separador)
            print("Saliendo del Sistema....")
            print(separador)


        