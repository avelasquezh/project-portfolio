# **Python Menu Calculator**

This is a small console project developed in Python. It uses a menu-based system to perform basic arithmetic operations. The project demonstrates programming logic, dictionaries for menu options, user input handling, and modular code with functions.

## **Features:**

- Provides a simple menu to choose operations.  
- Performs basic arithmetic operations: addition, subtraction, multiplication, and division.  
- Validates user input before executing operations.  
- Handles division by zero gracefully.  
- Interactive loop that allows multiple operations until the user exits.  

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

## **Execution:**

Clone the repository:

```bash
git clone https://github.com/avelasquezh/project-portfolio.git
cd your-repository-name
