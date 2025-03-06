"""
Clase para almacenar duraciones de tiempo (Duration)

Los objetos de esta clase representan intervalos de tiempo y se crean de la siguiente forma:

Ejemplos de creación:

    t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
    t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
    t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2.

Requisitos de la clase:

1. **Inicialización**
    - Debe permitir crear un objeto con horas, minutos y segundos.
    - Debe normalizar valores mayores a 59 en minutos y segundos.
    - Debe permitir crear un objeto a partir de otro objeto `Duration`.

2. **Propiedades y métodos:**
    - Implementar getters y setters mediante propiedades para:
      - `hours`: obtener y modificar las horas.
      - `minutes`: obtener y modificar los minutos (ajustando horas si es necesario).
      - `seconds`: obtener y modificar los segundos (ajustando minutos y horas si es necesario).
    
3. **Operaciones sobrecargadas:**
    - **Suma de objetos (`+`)**: el resultado será un nuevo objeto `Duration`.
    - **Resta de objetos (`-`)**: el resultado será un nuevo objeto `Duration`, asegurando que no haya valores negativos.

4. **Modificación del objeto actual:**
    - Métodos para sumar/restar horas, minutos y segundos:
      - `add_hours(h)`
      - `add_minutes(m)`
      - `add_seconds(s)`
      - `subtract_hours(h)`
      - `subtract_minutes(m)`
      - `subtract_seconds(s)`
    - Se deben ajustar los valores al modificar minutos o segundos.
    
5. **Representación en cadena:**
    - Método para devolver una cadena con el tiempo almacenado en formato:
      "10h 35m 5s"
      cuando la duración sea de 10 horas, 35 minutos y 5 segundos.

"""


from dataclasses import dataclass
from typing import Protocol

class DurationProtocol(Protocol):
    hours: int
    minutes: int
    seconds: int

@dataclass
class Duration:
    _hours: int = 0
    _minutes: int = 0
    _seconds: int = 0

    def __post_init__(self):
        self._normalize()

    def _normalize(self):
        total_seconds = self._hours * 3600 + self._minutes * 60 + self._seconds
        self._hours = total_seconds // 3600
        self._minutes = (total_seconds % 3600) // 60
        self._seconds = total_seconds % 60

    @property
    def hours(self) -> int:
        return self._hours

    @hours.setter
    def hours(self, value: int):
        self._hours = max(0, value)

    @property
    def minutes(self) -> int:
        return self._minutes

    @minutes.setter
    def minutes(self, value: int):
        self._minutes = value
        self._normalize()

    @property
    def seconds(self) -> int:
        return self._seconds

    @seconds.setter
    def seconds(self, value: int):
        self._seconds = value
        self._normalize()

    def __str__(self) -> str:
        return f"{self._hours}h {self._minutes}m {self._seconds}s"

    def __add__(self, other: DurationProtocol) -> "Duration":
        return Duration(self._hours + other.hours, self._minutes + other.minutes, self._seconds + other.seconds)

    def __sub__(self, other: DurationProtocol) -> "Duration":
        total_seconds = (self._hours * 3600 + self._minutes * 60 + self._seconds) - \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        return Duration(0, 0, max(0, total_seconds))

    def add_hours(self, h: int):
        self._hours += h

    def add_minutes(self, m: int):
        self._minutes += m
        self._normalize()

    def add_seconds(self, s: int):
        self._seconds += s
        self._normalize()

    def subtract_hours(self, h: int):
        self._hours = max(0, self._hours - h)

    def subtract_minutes(self, m: int):
        total_seconds = self._hours * 3600 + self._minutes * 60 + self._seconds - m * 60
        self.__init__(0, 0, max(0, total_seconds))

    def subtract_seconds(self, s: int):
        total_seconds = self._hours * 3600 + self._minutes * 60 + self._seconds - s
        self.__init__(0, 0, max(0, total_seconds))
