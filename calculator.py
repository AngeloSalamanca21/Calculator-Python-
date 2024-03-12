#Suma
def addition(num1, num2):
    return num1 + num2

#Resta
def subtract(num1, num2):
    return num1 - num2

#Multiplicación
def multiply(num1, num2):
    return num1 * num2

#División
def division(num1, num2):
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

    option = input("Ingresa el número de la operación que deseas realizar: ")

    if option == '5':
        print("¡Hasta luego!")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if option == '1':
        print("Resultado:", addition(num1, num2))
    elif option == '2':
        print("Resultado:", subtract(num1, num2))
    elif option == '3':
        print("Resultado:", multiply(num1, num2))
    elif option == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")