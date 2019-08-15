import csv
from play_ListaDoblemente import ListaDoble
from punteo_Pila import Pila
from puntuaciones_Cola import Cola
from usuarios_CircularDoble import CircualarDoble

lista = ListaDoble()
pila = Pila()
cola = Cola()
circular = CircualarDoble()


with open('C:/Users/sr281/OneDrive/Escritorio/EDD2SEMESTRE2019/archivo.csv', newline='')as archivo:
    reader = csv.DictReader(archivo)
   # print(archivo.read())
    for column in reader:
        circular.agregar_final(column['Usuarios'])
circular.recorrer1()
circular.graficar2()



"""lista.agregar_final("#")
lista.agregar_final("#")
lista.agregar_final("#")
lista.agregar_final("#")
lista.recorrer()
lista.garficar2()

pila.agregar_inicio(1)
pila.agregar_inicio(2)
pila.agregar_inicio(3)
pila.agregar_inicio(4)
pila.recorrerPila()
pila.agregar_inicio(100)
pila.recorrerPila()



pila.eliminar()
pila.eliminar()
pila.recorrerPila()
pila.graficar2()

cola.agregar_final("m",6)
cola.agregar_final("s",10)
cola.agregar_final("r",9)
cola.recorrerCola()
cola.agregar_final("R", 100)
cola.recorrerCola()
cola.eliminar()
cola.recorrerCola()
cola.graficar2()"""

"""circular.agregar_final("Steve")
circular.agregar_final("Makey")
circular.agregar_final("Ramirez")
circular.agregar_final("Ruano")
#circular.recorrer1()
circular.recorrer2()"""






