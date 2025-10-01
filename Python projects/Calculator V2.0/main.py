# main.py

from calculadora import Calculadora, DivisionPorCeroError, _Sumar, _Restar, Multiplicar, Dividir, Modulo

def inicializar_calculadora():
    """Define las operaciones y configura la calculadora (SRP)."""
    
    # Mapeo de opciones para el menú: (nombre_a_mostrar, objeto_operacion, nombre_interno)
    opciones_menu = {
        "1": ("Sumar", _Sumar(), "sumar"),
        "2": ("Restar", _Restar(), "restar"),
        "3": ("Multiplicar", Multiplicar(), "multiplicar"),
        "4": ("Dividir", Dividir(), "dividir"),
        "5": ("Modulo", Modulo(), "modulo")
    }
    
    # Diccionario de operaciones internas para la Calculadora
    operaciones_internas = {
        "sumar": _Sumar(),
        "restar": _Restar(),
        "multiplicar": Multiplicar(),
        "dividir": Dividir(),
        "modulo": Modulo()
    }
    
    # Inyección de dependencias de operaciones
    calc = Calculadora(operaciones=operaciones_internas)
    
    return calc, opciones_menu

def menu():
    """Maneja la lógica de la interfaz de usuario (SRP)."""
    
    calc, opciones = inicializar_calculadora()
    
    while True:
        print("\n--- Calculadora 2.0 ---\n")
        for key, (nombre, _, _) in opciones.items():
            print(f"{key}. {nombre}")
        print(f"{int(key)+1}. Salir\n")

        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "6":
            print("Gracias por usar la calculadora.")
            break

        if opcion_seleccionada not in opciones:
            print("Opción inválida.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            # Obtenemos el nombre interno de la operación a ejecutar
            _, _, nombre_operacion = opciones[opcion_seleccionada]
            
            # La Calculadora ejecuta la operación correspondiente
            resultado = calc.ejecutar_operacion(nombre_operacion, num1, num2)
            
            print(f"Resultado: {resultado}")
            
        except DivisionPorCeroError as e:
            print(f"Error de Cálculo: {e}")
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar números.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    menu()