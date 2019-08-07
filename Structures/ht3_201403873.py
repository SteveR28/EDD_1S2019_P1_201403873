class Nodo:
    def __init__(self, num=None, sig=None):
        self.num = num
        self.sig = sig

    def __str__(self):
        return(self.num)

class NodoCola:
    def __init__(self, nombre=None, num=None, sig=None):
        self.nombre = nombre
        self.num = num
        self.sig = sig

    def __str__(self):
        return"%s %s" %(self.nombre, self.num)

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

    def agregar_inicio(self, nombre):
        if self.vacia():
            self.primero = self.ultimo = NodoCircular(nombre)
        else:
            aux = NodoCircular(nombre)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero == aux
        self.__unir_nodos()

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




class pila:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento


        if self.cola != None:
            self.cola.sig = elemento

        self.cola = elemento

    def eliminar(self, num):
        if int(self.cabeza.num) == int(num1):
            self.cabeza = self.cabeza.sig
            return True
        else:
            aux = self.cabeza
            anterior = aux
            while aux != None:
                if int(aux.num) == int(num1):
                    anterior.sig = aux.sig
                    return True
                anterior = aux
                aux = aux.sig
        return False

class cola:
    def __init__(self):
        self.cola = None

        def agregar(self, elemento):
            if self.cola == None:
                self.cola == elemento

            if self.cola != None:
                self.cola.sig = elemento

            self.cola = elemento

    def eliminar(self, num):
        if int(self.cola.num) == int(num1):
            self.cola = self.cola.sig
            return True
        else:
            aux = self.cola
            anterior = aux
            while aux != None:
                if int(aux.num) == int(num1):
                    anterior.sig = aux.sig
                    return True
                anterior = aux
                aux = aux.sig
        return False

if __name__ == "__main__":
    ls = pila()
    co = cola()
    cir = CircualarDoble()

    while(True):
        print("Estructuras:\n"+
              "1. Pila\n"+
              "2. Cola\n"+
              "3. Circular")

        op =input("Ingrese la opcion: ")
        if op == "1":
            while (True):
                print("Opciones:\n" +
                      "1. Agregar\n" +
                      "2. Eliminar")

                a = input("Ingrese la opcion")
                if a == "1":
                    num1 = input("Ingrese el numero: ")
                    nod = Nodo(num1)
                    ls.agregar(nod)
                elif a == "2":
                    num1 = input("Ingrese elemento a eliminar: ")
                    if (ls.eliminar(num1)):
                        print("Eliminado")
                    else:
                        print("No encontrado")

        elif op == "2":
            while (True):
                print("Opciones:\n" +
                      "1. Agregar\n" +
                      "2. Eliminar")

                b = input("Ingrese la opcion")
                if b == "1":
                    num1 = input("Ingrese el numero: ")
                    nod = NodoCola(num1)
                    co.agregar(nod)
                elif b == "2":
                    num1 = input("Ingrese elemento a eliminar: ")
                    if (co.eliminar(num1)):
                        print("Eliminado")
                    else:
                        print("No encontrado")
        elif op == "3":
            while (True):
                print("Opciones:\n" +
                      "1. Agregar")

                b = input("Ingrese la opcion")
                if b == "1":
                    nom = input("Ingrese el nombre: ")
                    nod = NodoCola(nom)
                    cir.agregar_inicio(nod)






