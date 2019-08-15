"""with open('C:/Users/sr281/OneDrive/Escritorio/EDD2SEMESTRE2019/archivo.csv', 'r') as archivo:
    print(archivo.read())

    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for l in lineas:
        linea = l.split(',')
        print(linea)

import csv

with open('C:/Users/sr281/OneDrive/Escritorio/EDD2SEMESTRE2019/archivo.csv', 'r') as archivo:
    reader = csv.reader(archivo)
    us = archivo.line_buffering
    for row in reader:
        print("Usuario: {0}".format(row[0]))


# esto es el random
import random

class Food:
    def __init__(self):
        self.x_coordinate = random.randint(0,60)
        self.y_coordinate = random.randint(0,20)
        type = random.randint(0,40)
        if type <=5 :
            self.type_food = 0 #0 == bad food (*)
        else:
            self.type_food = 1 #1 == good food (+)

    def print(self):
        print('x-coordinate: ', self.x_coordinate)
        print('y-coordinate: ', self.y_coordinate)
        if self.type_food==1:
            print('food: good')
        else:
            print('food: bad')


for x in range(0, 10):
    food = Food()
    food.print()"""

