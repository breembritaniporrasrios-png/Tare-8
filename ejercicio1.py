class PilaArreglo:
    def __init__(self):
        self.datos = []

    def apilar(self, plato):
        self.datos.append(plato)

    def desapilar(self):
        if len(self.datos) == 0:
            return None
        return self.datos.pop()

    def ver_tope(self):
        if len(self.datos) == 0:
            return None
        return self.datos[-1]

    def mostrar(self):
        if len(self.datos) == 0:
            print("La pila esta vacia")
        else:
            print("Platos en la pila:")
            for i in range(len(self.datos) - 1, -1, -1):
                print(self.datos[i])


print("SOLUCION 1: PILA CON ARREGLO DINAMICO")

pila1 = PilaArreglo()

pila1.apilar("Plato 1")
pila1.apilar("Plato 2")
pila1.apilar("Plato 3")

pila1.mostrar()

print("Plato de arriba:")
print(pila1.ver_tope())

print("Retirando plato:")
print(pila1.desapilar())

pila1.mostrar()
