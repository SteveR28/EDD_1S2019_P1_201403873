class NodoPila:

    def __init__(self, punteo):
        self.punteo = punteo
        self.siguiente = None


class Pila:

    def __init__(self):
        self.primero = None
        self.size = 0

    def vacia(self):
        return  self.primero == None

    def agregar_inicio(self, punteo):
        if self.vacia():
            self.primero  = NodoPila(punteo)
        else:
            aux = NodoPila(punteo)
            aux.siguiente = self.primero
            self.primero = aux
        self.size += 1

    def recorrerPila(self):
        aux = self.primero
        while aux:
            print(aux.punteo)
            aux = aux.siguiente

    def size(self):
        return self.size()

    def eliminar(self): #este elimina al inicio
        if self.vacia():
            print("esta vacia")
        elif self.primero.siguiente == None:
            self.primero= self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1