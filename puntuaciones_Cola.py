import os

class NodoCola:

    def __init__(self, nombre, punteo):
        self.nombre = nombre
        self.punteo = punteo
        self.siguiente = None
        self.anterior = None

class Cola:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return  self.primero == None

    def agregar_final(self, nombre, punteo):
        if self.vacia():
            self.primero = self.ultimo = NodoCola(nombre, punteo)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoCola(nombre, punteo)
            self.ultimo.anterior = aux
        self.size += 1

    def recorrerCola(self):
        aux = self.primero
        while aux:
            print(aux.nombre)
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



    def graficar2(self):
        contenido = open('cola.txt', 'a')
        contenido.write('digraph G{\n')
        contenido.write('node [shape=box];\n')
        aux = self.primero
        x = 0
#        aux2 = self.primero.siguiente
        while(aux is not None):
            contenido.write("Usuario"+str(x)+" [label=\"Usuario: " + str(aux.nombre) +" punteo: " + str(aux.punteo) + "\"];\n")
            contenido.write("Usuario"+str(x)+"->Usuario"+str(x+1)+";\n")
            aux = aux.siguiente
            x+=1
            #aux2 = aux.siguiente
        contenido.write("}")
        contenido.close()
        os.system("dot -Tpng cola.txt -o cola.png")
