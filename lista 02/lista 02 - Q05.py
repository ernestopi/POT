"""Lista2_q5. Faça um programa que grave duas listas de 10 elementos numéricos inteiros cada uma
e intercale os elementos destas em uma outra lista de 20 elementos.
Obs: use uma função para gravar as listas e outra para intercalar
Exemplo:          l1 = [2, 6, 9]  l2 = [10, 5, 12]
lista intercalada l3 = [2, 10, 6, 5, 9, 12]
Obs: Fazer uma segunda versão função para intercalar sem usar o comando append"""
max_lista = 3
l1 = []
l2 = list(range(max_lista))

from random import randint

def gravar_listas(): # Grava as duas listas com valores randômicos entre 0 e 100
     for i in range (max_lista):
          l1.append(randint(0,100))
          l2[i] = randint(0,100)

# função para intercalar as duas listas usando append
def intercalar():
     l3 = []
     for i in range(max_lista):
         l3.append(l1[i])
         l3.append(l2[i])
     return l3

# função para intercalar as duas listas sem usar o append
def intercalar2():
     l3 = [0]*(2*max_lista)
     j = 0
     for i in range(max_lista):
         l3[j] = l1[i]
         j += 1
         l3[j] = l2[i]
         j += 1
     return l3

gravar_listas()
print("\nLista 1: ", l1)
print("\nLista 2: ", l2)
print("\nLista intercalada  : ", intercalar())
print("\nLista intercalada 2: ", intercalar2())