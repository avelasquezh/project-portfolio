# **Python Menu Calculator**

This is a small console project developed in Python. It uses a menu-based system to perform basic arithmetic operations. The project demonstrates programming logic, dictionaries for menu options, user input handling, and modular code with functions.

## **Features:**

- Provides a simple menu to choose operations.  
- Performs basic arithmetic operations: addition, subtraction, multiplication, and division.  
- Validates user input before executing operations.  
- Handles division by zero gracefully.  
- Interactive loop that allows multiple operations until the user exits.  

## **Skills:**

- **Functions & Modularization**: Separation of responsibilities (e.g., `inicializar_calculadora`, `menu`).  
- **Dependency Injection**: Operations (`Sumar`, `Restar`, `Multiplicar`, `Dividir`) are passed into the `Calculadora` class via a dictionary, making the system extensible.  
- **Tuples & Multiple Return Values**: Each menu option is represented as a tuple `(label, object, internal_name)` and functions return multiple values (`calc, opciones`).  
- **Dictionaries as Mappings**: Use of dictionaries to map menu options to operations.  
- **Conditionals** (`if`, `elif`, `else`) for flow control.  
- **Loops** (`while True`) for interactive user input until exit.  
- **Exception Handling**: Specific (`DivisionPorCeroError`, `ValueError`) and generic (`Exception`) handling for robustness.  
- **Type Casting (Casteo)**: Conversion of user input with `float(input(...))`.  
- **String Formatting (f-strings)**: Embedding variables inside strings for dynamic output (`print(f"Resultado: {resultado}")`).  
- **Variable Destructuring (Unpacking)**: Extracting tuple elements (`_, _, nombre_operacion = opciones[...]`).  
- **Separation of Concerns (SRP)**: The calculator logic is separated from the user interface logic.  
- **Error Messages & User Guidance**: Friendly messages guiding the user when errors occur.  

## **Execution:**

Clone the repository:

```bash
git clone https://github.com/avelasquezh/project-portfolio.git
cd your-repository-name
