# importo la librería math para utilizarla en los próximos ejercicios
import math


#----------------------------------------------------------------------------------------------------------------
# Ejercicio 1) Crear un programa que imprima por pantalla el mensaje: Hola Mundo!
#----------------------------------------------------------------------------------------------------------------
print("Ejercicio 1)")

print("Hola Mundo!")

#----------------------------------------------------------------------------------------
# Ejercicio 2) 
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado.
#----------------------------------------------------------------------------------------
print("Ejercicio 2)")

# Solicito al usuario que ingrese su nombre
nombre_usuario = input("Por favor ingrese su nombre: ")

# Imprimo el saludo
print(f"Hola {nombre_usuario}, es un gusto saludarte!")


#---------------------------------------------------------------------------------------------------------
# Ejercicio 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados
#---------------------------------------------------------------------------------------------------------
print("Ejercicio 3)")
# Solicito los datos del usuario
nombre           = input("Por favor, ingrese su nombre: ")
apellido         = input("Por favor, ingrese su apellido: ")
edad             = int(input("Por favor, ingrese su edad: "))
lugar_residencia = input("Por favor ingrese su lugar de residencia: ")

# Imprimo los datos del usuario
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")


#----------------------------------------------------------------------------------------------------------------
# Ejercicio 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su
# perímetro.
#-----------------------------------------------------------------------------------------------------------------
print("Ejercicio 4)")

radio = float(input("Por favor ingrese el radio del círculo para poder calcular su área y perímetro: "))

# Calculo el área y el perímetro utilizando la función math.pi
area      = round(math.pi * (radio)**2,2)
perimetro = round(2 * math.pi * radio,2)

# Imprimo el área y el perímetro
print(f"El área del círculo es : {area}")
print(f"El perímetro del círculo es : {perimetro}")


#-----------------------------------------------------------------------------------------------------------------
# Ejercicio 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas 
# horas equivale.
#-----------------------------------------------------------------------------------------------------------------
print("Ejercicio 5)")

segundos = float(input("Por favor ingrese la cantidad de segundos que desea convertir a horas: "))
horas    = round(segundos/3600,2)

print(f"{segundos} segundos equivalen a un total de {horas} horas.")


#-----------------------------------------------------------------------------------------------------------------
# Ejercicio 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de 
# dicho número.
# -----------------------------------------------------------------------------------------------------------------
print("Ejercicio 6)")

numero = int(input("Ingrese un número: "))

print(f"La tabla de multiplicar de {numero} es: ")
print(f"{numero} x 0 =",numero*0)
print(f"{numero} x 1 =",numero*1)
print(f"{numero} x 2 =",numero*2)
print(f"{numero} x 3 =",numero*3)
print(f"{numero} x 4 =",numero*4)
print(f"{numero} x 5 =",numero*5)
print(f"{numero} x 6 =",numero*6)
print(f"{numero} x 7 =",numero*7)
print(f"{numero} x 8 =",numero*8)
print(f"{numero} x 9 =",numero*9)
print(f"{numero} x 10 =",numero*10)


#-----------------------------------------------------------------------------------------------------------------
# Ejercicio 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el 
# resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
# -----------------------------------------------------------------------------------------------------------------
print("Ejercicio 7)")

numero1 = int(input("Ingrese un número entero distinto de 0(cero): "))
numero2 = int(input("Ingrese otro número entero distinto de 0(cero): "))

suma = numero1 + numero2
resta = numero1 - numero2
cociente = numero1 / numero2
producto = numero1 * numero2

print(f"El resultado de la suma de los números ingresados es: {suma}")
print(f"El resultado de la resta de los números ingresados es: {resta}")
print(f"El resultado de la division de los números ingresados es: {cociente}")
print(f"El resultado de la multiplicación de los números ingresados es: {producto}")


#-----------------------------------------------------------------------------------------------------------------
# Ejercicio 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa
# corporal. 
# -----------------------------------------------------------------------------------------------------------------
print("Ejercicio 8)")

altura = float(input("Ingrese su altura en Metros: "))
peso = float(input("Ingrese su peso en Kilogramos: "))

indice_masa_corporal = round(peso / altura**2, 2)

print(f"El Índice de Masa Corporal (IMC) es: {indice_masa_corporal}")


#-----------------------------------------------------------------------------------------------------------------
# Ejercicio 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla 
# su equivalente en grados Fahrenheit. 
#-----------------------------------------------------------------------------------------------------------------
print("Ejercicio 9)")

temperatura_grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_grados_fahrenheit = round(9/5 * temperatura_grados_celsius + 32,2)

print(f"{temperatura_grados_celsius}°C equivalen a {temperatura_grados_fahrenheit}° F")


#-----------------------------------------------------------------------------------------------------------------
# Ejercicio 10) 
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
#-----------------------------------------------------------------------------------------------------------------
print("Ejercicio 10)")

numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el segundo número: "))
numero3=float(input("Ingrese el tercer número: "))

suma=numero1 + numero2 + numero3
promedio = round(suma/3,2)

print(f"El promedio de los tres números ingresados es {promedio}")
