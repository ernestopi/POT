# criar função que recebe n1 e n2 e retorna a soma dos numeros inteiros
# contidos no intervalo.

# use a função em um programa q lê n1 e n2 do usuário e imprime a soma.

def soma_intervalo(n1, n2):
    soma = 0
    for c in range(n1, n2 + 1):
        soma += c

    return soma


while True:
    try:
        numero1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
        numero2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
        if numero2 < numero1:
            help = numero2
            numero2 = numero1
            numero1 = help
        print(f'{soma_intervalo(numero1, numero2)}')
        break



    except:
        print('DIGITE UM VALOR VÁLIDO')