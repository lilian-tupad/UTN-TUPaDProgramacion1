# Ejercicio N° 1 - Caja del Kiosco
# Alumna: Lilian Ruth Ismach


# Separador visual para la consola
separador = "-----------------------------------------------------------------"

# Nombre del programa
print(separador)
print("Caja del Kiosco")
print(separador)

# Validación del nombre del cliente (solo letras)
nombre_cliente = input("Nombre del Cliente: ").strip()
while not nombre_cliente.isalpha():
    print("Error: El nombre del cliente solo puede contener letras. Por favor, verifique el dato ingresado e intente nuevamente")
    nombre_cliente = input("Nombre del Cliente: ")

# Validación de la cantidad de productos (entero mayor a 0)
cantidad_productos = input("Cantidad de productos: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0: 
    print("Error: Por favor, ingrese una cantidad válida: debe ser un número entero mayor que 0.")
    cantidad_productos = input("Cantidad de productos: ")
cantidad_productos = int(cantidad_productos)

# Variables para los cálculos finales
total_sin_descuento = 0.0
total_con_descuento = 0.0

for contador_productos in range(1, cantidad_productos + 1):
    # Validación del precio (entero mayor a 0)
    precio = input(f"Producto N° {contador_productos} - Percio $: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Error: El precio ingresado no es válido. Ingrese un número entero mayor que 0, por favor.")
        precio = input(f"Producto N° {contador_productos} - Percio $: ")
    precio = int(precio)

    # Validación de la opción descuento
    descuento =input(f"Producto N° {contador_productos} - Precio ${precio} - Aplicar Descuento? Escriba 'S' (SI)/ 'N' (NO): ").upper()
    while not descuento in ('S','N'):
        print("Error: La opción ingresada no es válida. Por favor, escriba 'S' para aplicar descuento o 'N' si no desea aplicarlo.")
        descuento = input(f"Producto N° {contador_productos} - Precio ${precio} - Aplicar Descuento? Escriba 'S' (SI)/ 'N' (NO): ").upper()

    # Cálculo del total con y sin descuento
    total_sin_descuento += precio 
    if descuento == 'S':
        total_con_descuento += precio * 0.9
    else: 
        total_con_descuento += precio 

# Mensaje final
print(separador)
print("Detalles de la compra:")
print(separador)
print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuento $:{total_sin_descuento:.2f}")
print(f"Total con descuento $:{total_con_descuento:.2f}")
print(f"Ahorro $:{total_sin_descuento-total_con_descuento:.2f}")
print(f"Promedio por producto $:{total_con_descuento/cantidad_productos:.2f}")