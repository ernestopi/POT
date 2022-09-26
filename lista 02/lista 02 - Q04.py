from random import randint

max_lista = 15
l = list(range(max_lista))

#função para gerar a lista
def gravar_lista():
    for i in range (max_lista):
        l[i] = randint(0,100)
    return l

#função para encontrar o maior valora da lista
def maior():
    maior = l[0]
    pos_maior = 0
    for i in range(1, max_lista):
        if l[i] > maior:
            maior = l[i]
            pos_maior = i
    return maior, pos_maior

#função para encontrar o menor valor da lista
def menor():
    menor = l[0]
    pos_menor = 0
    for i in range (1,max_lista):
        if l[i] < menor:
            menor = l[i]
            pos_menor = i
    return menor , pos_menor

print(gravar_lista())
print(f'O maior número da lista é {maior()} e econtra-se na posição {maior()}')
print(f'O menorr número da lista é {menor()} e econtra-se na posição {menor()}')


