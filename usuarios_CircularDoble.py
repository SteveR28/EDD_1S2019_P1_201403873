class NodoCircular:

    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class CircualarDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar_final(self,nombre):
        if self.vacia():
            self.primero=self.ultimo= NodoCircular(nombre)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente= NodoCircular(nombre)
            self.ultimo.anterior=aux
        self.__unir_nodos()

    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer1(self):
        aux2 = self.primero
        while aux2:
            print(aux2.nombre)
            aux2 = aux2.siguiente
            if aux2 == self.primero:
                break

    def recorrer2(self):
        aux2 = self.ultimo
        while aux2:
            print(aux2.nombre)
            aux2 = aux2.anterior
            if aux2 == self.ultimo:
                break