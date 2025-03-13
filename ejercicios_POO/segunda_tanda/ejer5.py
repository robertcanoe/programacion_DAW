"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

- Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
- Obtener el número de elementos almacenados (tamaño).
- Saber si la pila o la cola está vacía.
- Vaciar completamente la pila o la cola.
- Para el caso de la pila:
   * Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
   * Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
   * Leer el elemento superior de la pila sin retirarlo (top).
- Para el caso de la cola:
   * Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
   * Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
   * Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).
"""
from typeguard import typechecked

class Stack:
    def __init__(self, initial_values: list[int] | None = None):
        self.__items = []
        if initial_values is not None:
            if not all(isinstance(x, int) for x in initial_values):
                raise ValueError("Todos los valores iniciales deben ser enteros")
            self.__items.extend(initial_values)

    def __str__(self) -> str:
        return f"Stack({self.__items})"
    
    @property
    @typechecked
    def items(self) -> list[int]:
        return self.__items.copy()

    @typechecked
    def push(self, value: int) -> None:
        self.__items.insert(0, value)

    @typechecked
    def pop(self) -> int:
        if not self.__items:
            raise ValueError("Stack.pop(): No se puede desapilar: la pila está vacía")
        return self.__items.pop(0)

    @typechecked
    def top(self) -> int:
        if not self.__items:
            raise ValueError("Stack.top(): No se puede leer el tope: la pila está vacía")
        return self.__items[0]

    @typechecked
    def is_empty(self) -> bool:
        return not self.__items

    @typechecked
    def empty(self) -> None:
        self.__items.clear()

    @typechecked
    def __len__(self) -> int:
        return len(self.__items)

class Queue:
    def __init__(self, initial_values: list[int] | None = None):
        self.__items = []
        if initial_values is not None:
            if not all(isinstance(x, int) for x in initial_values):
                raise ValueError("Todos los valores iniciales deben ser enteros")
            self.__items.extend(initial_values)

    @property
    @typechecked
    def items(self) -> list[int]:
        return self.__items.copy()

    @typechecked
    def enqueue(self, value: int) -> None:
        self.__items.append(value)

    @typechecked
    def dequeue(self) -> int:
        if not self.__items:
            raise ValueError("Queue.dequeue(): No se puede desencolar: la cola está vacía")
        return self.__items.pop(0)

    @typechecked
    def front(self) -> int:
        if not self.__items:
            raise ValueError("Queue.front(): No se puede leer el frente: la cola está vacía")
        return self.__items[0]

    @typechecked
    def is_empty(self) -> bool:
        return not self.__items

    @typechecked
    def empty(self) -> None:
        self.__items.clear()

    @typechecked
    def __len__(self) -> int:
        return len(self.__items)

if __name__ == "__main__":
   
    try:
        # Pruebas para Stack
        s = Stack([1, 2, 3])
        print("Stack inicial:", s.items)
        s.push(4)
        print("Después de push:", s.items)
        print("Tamaño:", len(s))
        print("¿Está vacía?", s.is_empty())
        print("Top:", s.top())
        print("Pop:", s.pop())
        print("Después de pop:", s.items)
        s.empty()
        print("Después de empty:", s.items)
        print("Intentando pop en pila vacía:")
        s.pop()  # esto lanza una excepción
    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Pruebas para Queue
        q = Queue([1, 2, 3])
        print("\nQueue inicial:", q.items)
        q.enqueue(4)
        print("Después de enqueue:", q.items)
        print("Tamaño:", len(q))
        print("¿Está vacía?", q.is_empty())
        print("Front:", q.front())
        print("Dequeue:", q.dequeue())
        print("Después de dequeue:", q.items)
        q.empty()
        print("Después de empty:", q.items)
        print("Intentando dequeue en cola vacía:")
        q.dequeue()  # esto lanza una excepción
    except ValueError as e:
        print(f"Error: {e}")