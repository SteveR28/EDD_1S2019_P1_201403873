class NodoListaDoble:

    def __init__(self,serp):
        self.serp = serp
        self.siguiente = None
        self.anterior = None

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return  self.primero == None

    def agregar_final(self,serp):
        if self.vacia():
            self.primero=self.ultimo = NodoListaDoble(serp)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoListaDoble(serp)
            self.ultimo.anterior = aux
        self.size += 1

    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.serp)
            aux = aux.siguiente

    def size(self):
        return self.size()



    def eliminar2(self): #este elimina al final
        if self.vacia():
            print("esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0

        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1
