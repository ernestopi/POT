from random import *
max_lista = 10
lista = list(range(max_lista))
quant_neg = 0; soma_pos = 0.0

for i in range(max_lista):
    while True:
        try:
            lista[i] = uniform(-100,100)
            if lista[i] < 0:
                quant_neg += 1
            else:
                soma_pos += lista[i]
            break
        except:
            print("Número inválid. Digite Novamente.")

print(f'A lista gerada: {lista}')
print(f'A quantidade de números negativos: {quant_neg}')
print(f'A soma dos números positivos: {soma_pos}')



