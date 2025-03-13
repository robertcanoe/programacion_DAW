"""
Clase para almacenar duraciones de tiempo (Duration)

Los objetos de esta clase representan intervalos de tiempo y se crean de la siguiente forma:

Ejemplos de creación:

    t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
    t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
    t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2.
"""

from typeguard import typechecked
from typing import Union

@typechecked
class Duration:
    def __init__(self, hours: Union[int, "Duration"] = 0, minutes: int = 0, seconds: int = 0) -> None:
        if isinstance(hours, Duration):
            self.__hours = hours.hours
            self.__minutes = hours.minutes
            self.__seconds = hours.seconds
        else:
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
        self._normalize()

    def _normalize(self) -> None:
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        self.__hours = total_seconds // 3600
        self.__minutes = (total_seconds % 3600) // 60
        self.__seconds = total_seconds % 60

    @property
    def hours(self) -> int:
        return self.__hours

    @hours.setter
    @typechecked
    def hours(self, value: int) -> None:
        self.__hours = max(0, value)

    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    @typechecked
    def minutes(self, value: int) -> None:
        self.__minutes = value
        self._normalize()

    @property
    def seconds(self) -> int:
        return self.__seconds

    @seconds.setter
    @typechecked
    def seconds(self, value: int) -> None:
        self.__seconds = value
        self._normalize()

    def __str__(self) -> str:
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"

    @typechecked
    def __add__(self, other: "Duration") -> "Duration":
        return Duration(self.__hours + other.hours, self.__minutes + other.minutes, self.__seconds + other.seconds)

    @typechecked
    def __sub__(self, other: "Duration") -> "Duration":
        total_seconds = (self.__hours * 3600 + self.__minutes * 60 + self.__seconds) - \
                       (other.hours * 3600 + other.minutes * 60 + other.seconds)
        return Duration(0, 0, max(0, total_seconds))

    @typechecked
    def add_hours(self, h: int) -> None:
        self.__hours += h

    @typechecked
    def add_minutes(self, m: int) -> None:
        self.__minutes += m
        self._normalize()

    @typechecked
    def add_seconds(self, s: int) -> None:
        self.__seconds += s
        self._normalize()

    @typechecked
    def subtract_hours(self, h: int) -> None:
        self.__hours = max(0, self.__hours - h)

    @typechecked
    def subtract_minutes(self, m: int) -> None:
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds - m * 60
        self.__init__(0, 0, max(0, total_seconds))

    @typechecked
    def subtract_seconds(self, s: int) -> None:
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds - s
        self.__init__(0, 0, max(0, total_seconds))

# Tests
if __name__ == "__main__":
    # Test 1: Creación y normalización
    t1 = Duration(1, 20, 30)
    print(f"Test 1 - Creación básica: {t1}")  

    t2 = Duration(2, 75, -10)
    print(f"Test 2 - Normalización: {t2}")  

    # Test 3: Copia de otro Duration
    t3 = Duration(t2)
    print(f"Test 3 - Copia: {t3}")  

    # Test 4: Suma
    t4 = t1 + t2
    print(f"Test 4 - Suma: {t4}")  

    # Test 5: Resta
    t5 = t2 - t1
    print(f"Test 5 - Resta: {t5}") 

    # Test 6: Modificación
    t6 = Duration(5, 30, 45)
    t6.add_minutes(90)
    print(f"Test 6 - Add minutes: {t6}")  

    t6.subtract_hours(8)
    print(f"Test 7 - Subtract hours: {t6}")