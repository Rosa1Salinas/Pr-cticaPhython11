def sumar (a, b):
    return a + b
def restar (a, b):
    return a - b
def dividir(a, b):
    if b== 0:
        return "Error: División por cero"
        return a / b
def multiplicar (a, b):
    return a * b
def mostrar_menu():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Salir")
    print(f"¡Hola, Rosita! Bienvenido.")
    print ("Hola Muchachos")
def calculadora():
    while True:
            mostrar_menu()
            opcion = input("Seleciona una opción (1-5): ")
            if opcion == '5':
                print("Saliendo de la calculadora. ¡Hasta luego!")
                break

                if opcion in ['1', '2', '3', '4']:
                    num1 = float(input("Introduce el primer número: "))
                    num2 = float(input("Introduce el segundo número: "))
                    if opcion == '1':
                        resultado = sumar(num1, num2)
                        print(f"El resultado de {num1} + {num2} es: {resultado}")
                    elif opcion == '2':
                        resultado = restar(num1, num2)
                        print(f"El resultado de {num1} - {num2} es: {resultado}")
                    elif opcion == '3':
                        resultado = dividir(num1, num2)
                        print(f"El resultado de {num1} / {num2} es: {resultado}")
                    elif opcion == '4':
                        resultado = multiplicar(num1, num2)
                        print(f"El resultado de {num1} * {num2} es: {resultado}")
                else:
                    print ("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
if __name__=="__main__":
    calculadora()


    
