# calculadora_simple.py

def sumar(a, b):
    """Realiza la suma de dos números."""
    return a + b

def restar(a, b):
    """Realiza la resta de dos números."""
    return a - b

def multiplicar(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b

def dividir(a, b):
    """Realiza la división de dos números. Maneja la división por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

def main():
    """Función principal para ejecutar la calculadora."""
    print("----- Calculadora Simple -----")

    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación deseada (1-5): ")

        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
        
        if opcion not in ('1', '2', '3', '4'):
            print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese solo números.")
            continue

        if opcion == '1':
            print(f"El resultado de la suma es: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"El resultado de la resta es: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
        elif opcion == '4':
            resultado_division = dividir(num1, num2)
            print(f"El resultado de la división es: {resultado_division}")
        
        input("\nPresione Enter para continuar...") # Pausa para ver el resultado

if __name__ == "__main__":
    main()
