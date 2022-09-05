def valor_s(t):
    s = 0
    for c in range(1, t + 1):
        s += (c ** 2 + 1) / (c + 3)
    return s.__round__(2)


while True:
    try:
        numero = int(input('DIGITE UM VALOR VÁLIDO '))
        if numero > 0:
            print(f'{valor_s(numero)}')
            break
        else:
            numero = int(input())
            print(f'{valor_s(numero)}')
            break


    except:
        print('DIGITE UM VALOR VÁLIDO ')


