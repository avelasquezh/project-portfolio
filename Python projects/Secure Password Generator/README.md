# Secure and Customizable Password Generator in Python

This project is a console password generator developed in Python. It goes beyond the basics, allowing the user to customize the password complexity and ensuring that the selected criteria are met. It demonstrates fundamental skills of a standard developer in logic, basic security, and robust user input handling.

## Features:

* **Customizable Length:** The user can specify the desired password length.
* **Selectable Character Types:** The user chooses whether to include uppercase letters, lowercase letters, numbers, and/or symbols.
* **Secure Generation:** Ensures that the password contains at least one character of each selected type (if applicable), to increase its strength.
* **Input Validation:** Handles invalid input for the length (non-numeric, negative).
* **Error Handling:** Informs the user if the password cannot be generated under the given conditions (e.g., insufficient length for the selected character types, or no type selected).
* **Interactive Console Interface:** Guides the user through the generation process.

## Demonstrated Skills (Standard Developer Level):

* **Modularization with Functions:** Design clean and reusable code through functions.
* **Advanced Handling of the `random` Module:** Use of `random.choice` and `random.shuffle` to ensure randomness and distribution.
* **String Manipulation (`string`):** Use of the `string` module to access predefined character sets.
* **Complex Flow Control:** Application of nested conditionals (`if`, `elif`, `else`) and loops (`while`) for program logic and iterative validation.
* **Robust Input and Output Handling:** Use of `input()` and `print()` with validation and `try-except` to prevent failures due to unexpected input (`ValueError`).
* **Security Concepts (Basic):** Application of principles for generating more secure passwords (mixing character types, suggested minimum length).
* **Business Logic Development:** Implementation of specific rules (e.g., ensuring the presence of selected character types).

## Execution:

1. **Clone the repository:**
```bash
git clone [[https://github.com/avelasquezh/Port.git](https://github.com/avelasquezh/Port.git](https://github.com/avelasquezh/project-portfolio.git)]
cd Port
```
*(Make sure you're in the correct project directory within the cloned repository.)*

2. **Run the Python script:**
Open your terminal or command line, navigate to the directory where you saved the `password_generator.py` file, and run the following command:
```bash
python password_generator.py
```

## Requirements:

* Python 3.x

## Author:

Arley Velasquez [https://www.linkedin.com/in/arley-velasquez-22822b36/](https://www.linkedin.com/in/arley-velasquez-22822b36/)
