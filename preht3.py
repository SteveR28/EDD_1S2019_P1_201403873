from pip._vendor.distlib.compat import raw_input


def array_sum():
    lista = []
    lista_suma = []
    suma = 0

    for i in range(5):
        elem = raw_input("ingrese digito: ")
        lista.append(elem)

    for j in lista:
        suma += int(j)
        lista_suma.append(suma)


    print('Method_1: ', lista_suma)

def staircase():
    n = int(input("cantidad "))
    print('Method_2:')
    for i in range(n+1):
        espacios = n-i
        print(' '*espacios+'*'*i)

def factorial(n2):

    if n2 == 1:
        return 1
    else:
        return n2 * factorial(n2-1)
print('Method_3: ',end='')
n2 = int(input("Numero: "))
print(factorial(n2))


def fibonacci(n3):
    if n3<2:
        return n3
    return fibonacci(n3-1)+fibonacci(n3-2)


array_sum()
staircase()


factorial(n2)
print('Method_4: ',end='')
for x in range(12):
    print(fibonacci(x),end=',')
print(fibonacci(12))