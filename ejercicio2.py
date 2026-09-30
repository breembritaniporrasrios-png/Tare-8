class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def __str__(self):
        return str(self.dato)


class PilaLista:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def desapilar(self):
        if self.tope is None:
            return None

        aux = self.tope
        self.tope = self.tope.siguiente
        return aux.dato

    def ver_tope(self):
        if self.tope is None:
            return None
        return self.tope.dato

    def mostrar(self):
        if self.tope is None:
            print("La pila esta vacia")
        else:
            print("Platos en la pila:")
            actual = self.tope
            while actual is not None:
                print(actual)
                actual = actual.siguiente


print()
print("SOLUCION 2: PILA CON LISTA ENLAZADA")

pila2 = PilaLista()

pila2.apilar("Plato A")
pila2.apilar("Plato B")
pila2.apilar("Plato C")

pila2.mostrar()

print("Plato de arriba:")
print(pila2.ver_tope())

print("Retirando plato:")
print(pila2.desapilar())

pila2.mostrar()
