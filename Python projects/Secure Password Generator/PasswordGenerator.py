# generador_contrasenas.py

import random
import string

def generar_contrasena(longitud, usar_mayusculas, usar_minusculas, usar_digitos, usar_simbolos):
    """
    Genera una contraseña segura y personalizable.
    Asegura que, si se selecciona un tipo de carácter, al menos uno de esos caracteres esté presente.

    Args:
        longitud (int): La longitud deseada para la contraseña.
        usar_mayusculas (bool): True para incluir letras mayúsculas.
        usar_minusculas (bool): True para incluir letras minúsculas.
        usar_digitos (bool): True para incluir números.
        usar_simbolos (bool): True para incluir símbolos.

    Returns:
        str: La contraseña generada o un mensaje de error si no se pueden cumplir las condiciones.
    """
    caracteres_posibles = []
    contrasena_generada_lista = []

    # Incluir y asegurar al menos un carácter de cada tipo seleccionado
    if usar_mayusculas:
        caracteres_posibles.extend(string.ascii_uppercase)
        contrasena_generada_lista.append(random.choice(string.ascii_uppercase))
    if usar_minusculas:
        caracteres_posibles.extend(string.ascii_lowercase)
        contrasena_generada_lista.append(random.choice(string.ascii_lowercase))
    if usar_digitos:
        caracteres_posibles.extend(string.digits)
        contrasena_generada_lista.append(random.choice(string.digits))
    if usar_simbolos:
        caracteres_posibles.extend(string.punctuation)
        contrasena_generada_lista.append(random.choice(string.punctuation))

    # Verificar que se haya seleccionado al menos un tipo de carácter
    if not caracteres_posibles:
        return "Error: Debe seleccionar al menos un tipo de carácter para generar la contraseña."
    
    # Asegurarse de que la longitud es suficiente para los caracteres obligatorios
    if longitud < len(contrasena_generada_lista):
        return f"Error: La longitud ({longitud}) es demasiado corta para incluir todos los tipos de caracteres seleccionados ({len(contrasena_generada_lista)})."

    # Llenar el resto de la contraseña con caracteres aleatorios de los posibles
    for _ in range(longitud - len(contrasena_generada_lista)):
        contrasena_generada_lista.append(random.choice(caracteres_posibles))

    # Mezclar la contraseña para asegurar la aleatoriedad de la posición de los caracteres obligatorios
    random.shuffle(contrasena_generada_lista)

    return "".join(contrasena_generada_lista)

def main():
    """
    Función principal para interactuar con el usuario y gestionar la generación de contraseñas.
    """
    print("----- Generador de Contraseñas Seguras y Personalizables -----")

    while True:
        try:
            longitud_str = input("Ingrese la longitud deseada para la contraseña (mínimo 8 caracteres recomendado): ")
            longitud = int(longitud_str)
            if longitud < 1:
                print("La longitud debe ser un número positivo. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la longitud.")

    print("\nSeleccione los tipos de caracteres a incluir (s/n):")
    usar_mayusculas = input("¿Incluir letras MAYÚSCULAS? (s/n): ").lower() == 's'
    usar_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_digitos = input("¿Incluir NÚMEROS? (s/n): ").lower() == 's'
    usar_simbolos = input("¿Incluir SÍMBOLOS (!@#$%)? (s/n): ").lower() == 's'

    if not (usar_mayusculas or usar_minusculas or usar_digitos or usar_simbolos):
        print("¡Atención! Debe seleccionar al menos un tipo de carácter para generar una contraseña.")
        input("Presione Enter para salir y volver a intentar...")
        return # Sale del programa si no hay selección

    contrasena = generar_contrasena(longitud, usar_mayusculas, usar_minusculas, usar_digitos, usar_simbolos)
    
    # Manejar posibles mensajes de error de la función generar_contrasena
    if "Error:" in contrasena:
        print(contrasena)
    else:
        print(f"\nSu contraseña generada es: {contrasena}")
        print("\n¡Recuerde guardarla en un lugar seguro!")
    
    input("\nPresione Enter para finalizar...")

if __name__ == "__main__":
    main()
