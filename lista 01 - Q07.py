def fatorial_func(fatorial):
    fatorial_final = 1
    for c in range(fatorial, 1, -1):
        fatorial_final *= c
    return fatorial_final


while True:
    try:
        fatorial = int(input())
        ch = fatorial_func(fatorial)
        print(ch)
        break

    except:
        print('Valor inválido, entre com um número inteiro')

