# **Python Menu Calculator**

This is a console-based calculator project developed in Python.  
It demonstrates not only arithmetic operations and error handling, but also **Object-Oriented Programming (OOP)**, **SOLID principles**, and clean code practices.

## **Features:**

- Menu-driven system to select mathematical operations.  
- Performs arithmetic operations: addition, subtraction, multiplication, division, and modulo.  
- Handles division by zero with a custom exception.  
- Validates user input to ensure numeric values.  
- Interactive loop to perform multiple operations until the user decides to exit.  

## **Skills:**

- **Functions & Modularization**: Clear separation of responsibilities (e.g., `initialize_calculator`, `menu`).  
- **Dependency Injection**: Operations (`Sum`, `Subtract`, `Multiply`, `Divide`) are injected into the `Calculator` class via a dictionary, making the system extensible and decoupled.  
- **Object-Oriented Programming (OOP)**: Use of **classes and objects** to model the calculator and its operations.  
- **Inheritance**: Operation classes inherit from a common base class (e.g., `Operation`), ensuring consistency.  
- **Polymorphism**: `operation.execute(num1, num2)` dynamically calls the appropriate subclass method at runtime.  
- **SOLID Principles**:  
  - **S**ingle Responsibility (SRP): Each class has a single responsibility (either one operation or calculator management).  
  - **O**pen/Closed (OCP): Open to extension (adding new operations) without modifying existing code.  
  - **L**iskov Substitution (LSP): Any subclass of `Operation` can replace the parent class without breaking functionality.  
  - **I**nterface Segregation (ISP): Operations only implement what they need (`execute`).  
  - **D**ependency Inversion (DIP): The calculator depends on abstractions, not concrete implementations.  
- **KISS Principle**: Simple, clean design without unnecessary complexity.  
- **Tuples & Multiple Return Values**: Menu options use tuples `(label, object, internal_name)`, and functions return multiple values (`calc, options`).  
- **Dictionaries as Mappings**: Menu keys map directly to operation classes.  
- **Conditionals** (`if`, `elif`, `else`) for decision-making.  
- **Loops** (`while True`) for repeated execution until exit.  
- **Exception Handling**:  
  - Custom errors (`DivisionByZeroError`, `ValueError`).  
  - Generic handling (`Exception`) for robustness.  
- **Type Casting**: Conversion of user input with `float(input(...))`.  
- **String Formatting (f-strings)**: Embedding variables inside strings for dynamic output (`print(f"Result: {result}")`).  
- **Variable Destructuring (Unpacking)**: Extracting tuple elements (`_, _, operation_name = options[...]`).  
- **Error Messages & User Guidance**: Friendly messages to guide users during errors.  
- **Separation of Concerns**: Logic (calculator) is separate from presentation (menu/printing).  

### **Programming Concepts**
- **Functions & Modularization**: Clear separation of responsibilities (`inicializar_calculadora`, `menu`).  
- **Dictionaries as Mappings**: Associating user menu options with operations and logic.  
- **Tuples & Multiple Return Values**: Storing operation metadata `(label, object, internal_name)`.  
- **Conditionals & Loops**: `if-elif-else` and `while True` for control flow and interactivity.  
- **Type Casting (Casteo)**: Converting user input with `float()`.  
- **String Formatting**: Use of **f-strings** for dynamic messages.  
- **Variable Destructuring (Unpacking)**: Extracting tuple elements (`_, _, nombre_operacion = ...`).  
- **Exception Handling**: Specific (`DivisionPorCeroError`, `ValueError`) and generic (`Exception`).  

### **Object-Oriented Programming (OOP)**
- **Encapsulation**: Operations are encapsulated as classes (`_Sumar`, `_Restar`, `Multiplicar`, `Dividir`, `Modulo`).  
- **Polymorphism**: Each operation inherits from the abstract base class `Operacion` and overrides `ejecutar()`.  
- **Abstraction**: The base class `Operacion` defines the interface for all operations.  
- **Dependency Injection**: `Calculadora` receives its operations externally, promoting flexibility.  

### **SOLID Principles**
- **SRP (Single Responsibility Principle)**: Each class or function has a single, well-defined purpose.  
- **OCP (Open/Closed Principle)**: The calculator is open to extension (adding new operations) but closed to modification.  
- **DIP (Dependency Inversion Principle)**: `Calculadora` depends on abstractions (`Operacion`), not concrete implementations.  

### **Clean Code & Best Practices**
- **KISS (Keep It Simple, Stupid)**: The design avoids unnecessary complexity.  
- **Readability**: Clear naming conventions and docstrings.  
- **Error Messages & User Guidance**: Friendly feedback for invalid input or unexpected errors.  
- **Separation of Concerns**: User interface logic is separated from core calculator logic.  
>>>>>>> 652b355f65d7d08fd6a3c59a71a2da8028c4cd5d

## **Execution:**

Clone the repository:

```bash
git clone https://github.com/avelasquezh/project-portfolio.git
cd your-repository-name
