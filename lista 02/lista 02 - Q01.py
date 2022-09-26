"""1) Faça um programa em python que tenha:
a) Uma função para criar/gravar uma lista com 100 elementos numéricos inteiros;
b) Uma função para mostrar a quantidade de números pares e números ímpares;
c) Uma função para gerar duas outras listas, uma lista somente com os números
   pares da lista original e outra lista somente com os números ímpares;
d) Função para mostrar o maior elemento da lista original;
e) Mostrar as 3 listas no programa principal. """
max_lista = 5
l = list(range(max_lista))
# l = []
l_p = []
l_i = []
from random import *


# a)
def gravar_lista():
    for i in range(max_lista):
        #        l[i] = int(input("\nDigite o  %dº número: " % (i+1)))
        l[i] = randint(-100, 100)  # gera números inteiros aleatórios


#        l[i] = uniform(-100,100)      gera números reais aleatórios
#         l.append(randint(-100,100))
# b)
def quant_p_i():
    cont_par = 0
    cont_impar = 0
    for i in range(max_lista):
        if l[i] % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
    print("\nQuantidade de números pares: %d." % cont_par)
    print("\nQuantidade de números ímpares: %d." % cont_impar)


# c)
def gerar_duas_listas():
    for i in range(max_lista):
        if l[i] % 2 == 0:
            l_p.append(l[i])
        else:
            l_i.append(l[i])


# d)
def maior():
    maior = l[0]
    for i in range(1, max_lista):
        if l[i] > maior:
            maior = l[i]
    print("\nMaior número da lista l: %d." % maior)


gravar_lista()
quant_p_i()
gerar_duas_listas()
maior()
print("Lista L: ", l)
print("Pares (Lista l_p): ", l_p)
print("Impares (Lista l_i): ", l_i)