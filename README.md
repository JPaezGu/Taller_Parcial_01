# Autor: Juan Camilo Páez Guaspud
# Taller Parcial #01 - Programación Orientada a Objetos

# Se realiza un taller calificativo que tiene como fin verificar que se haya aprendido los temas vistos anteriormente en clase:


# ____________ Parte A __________________________
    .
1. ("a.x, a._y, a._A__z") existen.
   
   * "a.__z" no existe directamente porque se transforma en "_A__z".
   * Los atributos con "__" sufren name mangling para evitar colisiones en herencia.
   
   el name mangling es la manipulación de nombres, una técnica que codifica la información de una función o variable en su nombre, creando un identificador único para el enlazador. Varias funciones pueden compartir el mismo nombre si su lista de parámetros difieren (sobrecarga de funciones).
____________________________________________________________________________________________________________
-
2. Imprime "False True"
-                                          
    * "__secret" no aparece como atributo directo
    * Con name mangling sí existe como "_A__secret"
____________________________________________________________________________________________________________
-
3.  * a. Falso: "_" es convención, no limita acceso real.
    * b. Falso: "__" no impide, solo renombra.
    * c. Verdadero: el mangling depende del nombre de la clase ("_Clase__atributo").
____________________________________________________________________________________________________________
-
4. Imprime "abc".
-
    * "_token" es accesible porque el guion bajo solo está protegido por convención.
    * "Subclases" pueden leerlo sin problema.
____________________________________________________________________________________________________________
5. Resultado: ("2, 1")
-
    * "self.__v" en Sub pasa a "_Sub__v = 2".
    * "self._Base__v = 1" viene de la clase base.
    * Cada clase mantiene su propia versión del atributo “privado”.
____________________________________________________________________________________________________________
-
6. Error: "AttributeError" en c.y
*
    * "__slots__" restringe los atributos solamente a ('x',)
    * Así se evita añadir nuevos atributos dinámicos.
____________________________________________________________________________________________________________
-
7. Debe ser: self._protegido = 99
-
    * Un solo guion bajo indica "uso interno" por convención.
____________________________________________________________________________________________________________
-
8. Imprime: "True False True"
-
    * "_step" existe y es accesible.
    * "__tick" no existe como tal, pero "_M__tick" sí, por mangling.
____________________________________________________________________________________________________________
-
9. Línea Solicitada: print(s._S__data)
-
    * El atributo privado "__data" se guarda como "_S__data"
____________________________________________________________________________________________________________
-
10. Es más probable: "_D__a"
-
    * "__a" se transforma en "_D__a"
    * Por eso aparece en "dir()"

# _____ Parte B __________________________________
-
A pesar de que @property no se abarcó con profundidad en clase, estos son los resultados de mi estudio:
-
11. Propiedades con Validación:
-
```python
@property
def saldo(self):
    return self._saldo

@saldo.setter
def saldo(self, value):
    if value < 0:
        raise ValueError("Saldo no puede ser negativo")
    self._saldo = value
```
-
    * Se asegura que el saldo nunca vaya a ser menor que cero.
____________________________________________________________________________________________________________
-
12. Propiedad:
-
```python
@property
def temperatura_f(self):
    return self._c * 9/5 + 32
```
-
    * Únicamente para lectura, se calcula dinámicamente desde °C.
____________________________________________________________________________________________________________
-
13. Invariante con Tipo:
-
```python
@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, value):
    if not isinstance(value, str):
        raise TypeError("nombre debe ser str")
    self._nombre = value
```
-
    * Se asegura que el atributo siempre sea una cadena.
____________________________________________________________________________________________________________
-
14. Encapsulación de colección:
-
```python
@property
def items(self):
    return tuple(self.__items)
```
-
    * Devuelve una tupla inmutable para proteger la lista interna. Su uso puede verse en la lista de transacciones en una cuenta bancaria de una app finaciera,En un catálogo de productos en una tienda online, etc.

# _____ Parte C __________________________________
-
15. Refactor a encapsulación:
-
```python
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
```
-
    * Se controla el valor asignado.
____________________________________________________________________________________________________________
-
16. Elección de Convección:
-
En una API pública de una librería:

    * Usaría "_atributo" cuando quiero indicar claramente que algo es interno, pero que aún puede usarse bajo responsabilidad del usuario. Esto es útil si un usuario avanzado quiere hacer debug o experimentar.

    * Usaría "__atributo" cuando quiero proteger el diseño interno de colisiones accidentales en herencia. Sirve en clases que serán heredadas y donde no quiero que los nombres internos choquen con atributos definidos por el usuario de la librería. Así, si alguien hace una subclase, no puede sobreescribir sin querer los atributos internos.
____________________________________________________________________________________________________________
-
17. Problema: devuelve lista mutable, se podría llamar una fuga de encapsulación
-
    *  Corrección: "return tuple(self._data)" o "return self._data.copy()"
____________________________________________________________________________________________________________
-
18. Diseño con Herencia y Mangling:
-
    * Falla en "B.get" porque "self.__x" se traduce a "_B__x" , distinto de "_A__x"

    * Solución: usar "_A__x" o cambiar a "_x" en la base.
____________________________________________________________________________________________________________
-
19. Composición y Fachada:
-
```python
class Servicio:
    def __init__(self):
        self.__repo = _Repositorio()

    def guardar(self, k, v):
        self.__repo.guardar(k, v)
```
-
    * Solo expone "guardar", manteniendo oculto "_dump"
____________________________________________________________________________________________________________
-
20. Mini-kata:
-
```python
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
-
    * En el código se protege el estado y se encapsula la lógica de logging.