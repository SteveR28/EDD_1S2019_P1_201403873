class Nodo:
    def __init__(self, num=None, sig=None):
        self.num = num
        self.sig = sig

    def __str__(self):
        return(self.num)

class lSimples:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento


        if self.cola != None:
            self.cola.sig = elemento

        self.cola = elemento

    def listar(self):
        aux = self.cabeza
        while aux != None:
            print(aux)
            aux = aux.sig

    def buscar(self, num):
        aux= self.cabeza
        while aux != None:
            if int(aux.num) == int(num1):
                return aux
            aux = aux.sig
        return None

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


if __name__ == "__main__":
    ls = lSimples()

    while(True):
        print("Menu:\n"+
              "1. Agregar\n"+
              "2. Listar\n"+
              "3. Buscar\n"+
              "4. Eliminar")

        a = input("Ingrese la opcion")
        if a == "1":
            num1 = input("Ingrese el numero: ")
            nod = Nodo(num1)
            ls.agregar(nod)
        elif a == "2":
            ls.listar()
        elif a =="3":
            num1 = input("Ingrese el numero a buscar: ")
            result = ls.buscar(num1)
            if result is not None:
                print(result)
            else:
                print("No encontrado \n")
        elif a == "4":
            num1 = input("Ingrese elemento a eliminar: ")
            if(ls.eliminar(num1)):
                print("Eliminado")
            else:
                print("No encontrado")

