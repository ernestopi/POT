'''6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média.'''

from random import *

#função para criar a lista quantidade
def lista_quantidades(quantidade):
    for i in range(20):
        quantidade.append(randint(1, 150))

#função para criar a lista preço
def lista_precos(preco):
    for i in range(20):
        preco.append(uniform(1.00, 999.0))

#função para calcular o faturamento
def calcula_faturamento(preco, quantidade):
    fat = []
    total = 0
    for i in range(20):
        total_por_produto = preco[i] * quantidade[i]
        total += total_por_produto
        fat.append(total_por_produto.__round__(2))
    return fat, total

#função para calcular a media do faturamento
def calcula_media_faturamento(total_fat, ls_quantidade): #função recebe total do faturamento e a quantidade
    total_qtd = len(ls_quantidade) #total de quantidade rececebe o tamanho da lista
    media = total_fat / total_qtd #media recebe total do faturamento dividido pelo total de quantidade
    return media #retorna a media

#função faturamento
def faturamentos_abaixo_da_media(fat, md):
    ls_abaixo_media = []
    for f in fat:
        if f < md:
            ls_abaixo_media.append(f)
    return ls_abaixo_media


def main():
    lista_preco = []
    lista_quantidade = []
    lista_quantidades(lista_quantidade)
    lista_precos(lista_preco)
    faturamento, total_faturamento = calcula_faturamento(lista_preco, lista_quantidade)
    media_faturamento = calcula_media_faturamento(total_faturamento, lista_quantidade)
    abaixo_media = faturamentos_abaixo_da_media(faturamento, media_faturamento)

    print(f'Faturamento:\n R$ {faturamento}')
    print(f'O faturamento total é igual a:\n R$ {total_faturamento:.2f}')

    print(f"A média do faturamento é igual a:\n R$ {media_faturamento:.2f}")

    print(f"Faturamentos que estão abaixo da média:\n{abaixo_media}")

    print(f"Faturamento total: R$ {sum(faturamento):.2f}")
    print(f'Faturamento Méido é igual a: R$ {sum(faturamento) / len(lista_quantidade):.2f}')


main()