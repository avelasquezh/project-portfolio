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

## **Execution:**

Clone the repository:

```bash
git clone https://github.com/avelasquezh/project-portfolio.git
cd your-repository-name
