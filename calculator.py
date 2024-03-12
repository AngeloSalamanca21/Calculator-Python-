#Suma
def sumar(num1, num2):
    return num1 + num2

#Resta
def restar(num1, num2):
    return num1 - num2

#Multiplicación
def multiplicar(num1, num2):
    return num1 * num2

#División
def dividir(num1, num2):
    #División por cero
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    else:
        return num1 / num2

#Opciones
while True:
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(num1, num2))
    elif opcion == '2':
        print("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")