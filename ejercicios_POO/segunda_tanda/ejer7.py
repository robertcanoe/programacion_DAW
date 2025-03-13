"""
7. Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos hacer las siguientes operaciones:

    - Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye simplificada, no se puede dividir por cero.
    - Obtener resultado de la fracción (número real).
    - Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
    - Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
    - Comparar fracciones entre sí o con enteros usando los operadores relacionales.

"""

from typeguard import typechecked

@typechecked
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
        
        sign = 1 if (numerator < 0 and denominator < 0) or (numerator >= 0 and denominator > 0) else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        divisor = self._calculate_gcd(numerator, denominator)
        self._numerator = sign * (numerator // divisor)
        self._denominator = denominator // divisor
    
    def _calculate_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    @property
    def numerator(self) -> int:
        return self._numerator
    
    @property
    def denominator(self) -> int:
        return self._denominator
    
    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"
    
    def __repr__(self) -> str:
        return f"Fraction({self._numerator}, {self._denominator})"
    
    def to_real(self) -> float:
        return self._numerator / self._denominator
    
    def __mul__(self, other) -> 'Fraction':
        if isinstance(other, Fraction):
            numerator = self._numerator * other._numerator
            denominator = self._denominator * other._denominator
        elif isinstance(other, int):
            numerator = self._numerator * other
            denominator = self._denominator
        else:
            raise TypeError("Can only multiply by another fraction or integer.")
        return Fraction(numerator, denominator)
    
    def __truediv__(self, other) -> 'Fraction':
        if isinstance(other, Fraction):
            if other._numerator == 0:
                raise ValueError("Cannot divide by zero.")
            numerator = self._numerator * other._denominator
            denominator = self._denominator * other._numerator
        elif isinstance(other, int):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            numerator = self._numerator
            denominator = self._denominator * other
        else:
            raise TypeError("Can only divide by another fraction or integer.")
        return Fraction(numerator, denominator)
    
    def __add__(self, other) -> 'Fraction':
        if isinstance(other, Fraction):
            numerator = self._numerator * other._denominator + other._numerator * self._denominator
            denominator = self._denominator * other._denominator
        elif isinstance(other, int):
            numerator = self._numerator + other * self._denominator
            denominator = self._denominator
        else:
            raise TypeError("Can only add another fraction or integer.")
        return Fraction(numerator, denominator)
    
    def __sub__(self, other) -> 'Fraction':
        if isinstance(other, Fraction):
            numerator = self._numerator * other._denominator - other._numerator * self._denominator
            denominator = self._denominator * other._denominator
        elif isinstance(other, int):
            numerator = self._numerator - other * self._denominator
            denominator = self._denominator
        else:
            raise TypeError("Can only subtract another fraction or integer.")
        return Fraction(numerator, denominator)
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Fraction):
            return self.to_real() < other.to_real()
        elif isinstance(other, int):
            return self.to_real() < float(other)
        else:
            raise TypeError("Can only compare with another fraction or integer.")
    
    def __le__(self, other) -> bool:
        if isinstance(other, Fraction):
            return self.to_real() <= other.to_real()
        elif isinstance(other, int):
            return self.to_real() <= float(other)
        else:
            raise TypeError("Can only compare with another fraction or integer.")
    
    def __gt__(self, other) -> bool:
        if isinstance(other, Fraction):
            return self.to_real() > other.to_real()
        elif isinstance(other, int):
            return self.to_real() > float(other)
        else:
            raise TypeError("Can only compare with another fraction or integer.")
    
    def __ge__(self, other) -> bool:
        if isinstance(other, Fraction):
            return self.to_real() >= other.to_real()
        elif isinstance(other, int):
            return self.to_real() >= float(other)
        else:
            raise TypeError("Can only compare with another fraction or integer.")
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Fraction):
            return self._numerator == other._numerator and self._denominator == other._denominator
        elif isinstance(other, int):
            return self._numerator == other and self._denominator == 1
        else:
            return False

# test usage
if __name__ == "__main__":
    f1 = Fraction(1, 5) 
    f2 = Fraction(1, 3)
    print(f1) 
    print(f2)  
    print(f1.to_real())
    print(f1 * 5) 
    print(f1 + f2)
    print(f1 > f2)
    print(f1 == 2) 