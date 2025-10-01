# calculadora.py
from typing import Callable, Dict

# Excepción personalizada (SRP: Responsabilidad Única)
class DivisionPorCeroError(Exception):
    """Excepción personalizada para división por cero."""
    pass

# Abstracción de Operación (OCP: Abierto/Cerrado)
class Operacion:
    """Clase base para cualquier operación."""
    def ejecutar(self, a: float, b: float) -> float:
        raise NotImplementedError

# Implementaciones concretas de operaciones
class _Sumar(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a + b

class _Restar(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a - b

class Multiplicar(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a * b

class Dividir(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionPorCeroError("No se puede dividir por cero.")
        return a / b
    

class Modulo(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a % b

# Clase Calculadora (SRP: Solo Gestiona y Ejecuta)
class Calculadora:
    """Gestiona y ejecuta operaciones matemáticas."""
    
    def __init__(self, operaciones: Dict[str, Operacion]):
        # Inyección de dependencias (Cumple OCP y DIP)
        self.operaciones = operaciones

    def ejecutar_operacion(self, nombre_operacion: str, num1: float, num2: float) -> float:
        if nombre_operacion not in self.operaciones:
            raise ValueError(f"Operación '{nombre_operacion}' no soportada.")
            
        operacion = self.operaciones[nombre_operacion]
        return operacion.ejecutar(num1, num2)