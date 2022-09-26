"""Lista2_q10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra."""

max_lista = 5
l = list(range(max_lista))


def gravar_lista(l):
    for i in range(max_lista):
        l[i] = int(input("\nDigite o %dº número: " % (i + 1)))


def determinar_maior(l):
    maior = l[0]
    for i in range(1, max_lista):
        if l[i] >= maior:
            maior = l[i]
            pos_maior = i
    return maior, pos_maior


def determinar_menor(l):
    menor = l[0]
    for i in range(1, max_lista):
        if l[i] <= menor:
            menor = l[i]
            pos_menor = i
    return menor, pos_menor


gravar_lista(l)
print("\nMaior número: %d. Posição: %d. " % determinar_maior(l))
print("\nMenor número: %d. Posição: %d. " % determinar_menor(l))