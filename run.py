def operacion(num1, num2, opcion):
    if opcion == 1:
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == 2:
        resultado = num1 * num2
        print(f"El producto de {num1} y {num2} es: {resultado}")
    else:
        print("Opción no válida. Por favor, ingrese 1 o 2.")

def main():
    print("Bienvenido a mi primer programa de mi Curso De POO")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    opcion = int(input("Seleccione la operación:\n1. Suma\n2. Multiplicación\nIngrese el número de la opción: "))

    operacion(num1, num2, opcion)

if __name__ == "__main__":
    main()
