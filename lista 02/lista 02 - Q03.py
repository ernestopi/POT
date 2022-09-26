from random import *

max_lista = 5
lista = list(range(max_lista))

#função para criar a lista
def gravar_lista():
    for i in range(max_lista):
        lista[i] = randint(1,100)

#função para inverter os elementos da lista
def inverter(lista):
    inverso = []
    for i in lista:
        inverso.insert(0, i)
    return inverso


print(lista)

print(inverter(lista))
