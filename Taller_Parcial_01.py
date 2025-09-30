# Autor: Juan Camilo Páez Guaspud
# Taller Parcial #01 - Programación Orientada a Objetos

# Se realiza un taller calificativo que tiene como fin verificar que se haya aprendido los temas vistos anteriormente en clase:


# 11. Propiedades con Validación:
@property
def saldo(self):
    return self._saldo

@saldo.setter
def saldo(self, value):
    if value < 0:
        raise ValueError("Saldo no puede ser negativo")
    self._saldo = value
# Se asegura que el saldo nunca vaya a ser menor que cero.

# 12. Propiedad:
@property
def temperatura_f(self):
    return self._c * 9/5 + 32
# Únicamente para lectura, se calcula dinámicamente desde °C.

# 13. Invariante con Tipo:
@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, value):
    if not isinstance(value, str):
        raise TypeError("nombre debe ser str")
    self._nombre = value
# Se asegura que el atributo siempre sea una cadena.

# 14. Encapsulación de colección:
@property
def items(self):
    return tuple(self.__items)
# Devuelve una tupla inmutable para proteger la lista interna

# 15. Refactor a encapsulación:
class Motor:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, v):
        if 0 <= v <= 200:
            self._velocidad = v
        else:
            raise ValueError("Velocidad fuera de rango")
# Se controla el valor asignado.

# 19. Composición y Fachada:
class Servicio:
    def __init__(self):
        self.__repo = _Repositorio()

    def guardar(self, k, v):
        self.__repo.guardar(k, v)
# Solo expone "guardar", manteniendo oculto "_dump"

# 20. Mini-kata:
class ContadorSeguro:
    def __init__(self):
        self._n = 0   # atributo protegido por convención

    def inc(self):
        self._n += 1
        self.__log()

    @property
    def n(self):
        return self._n   # solo lectura

    def __log(self):
        print("tick")   # método privado

def main():
    c = ContadorSeguro()
    c.inc()
    c.inc()
    print("Valor final del contador:", c.n)

if __name__ == "__main__":
    main()

# En el código se protege el estado y se encapsula la lógica de logging.