def divisores(n):
    quant = 0
    for i in range(1, n+1):
        if n % i == 0:
            print("\n%d é divisivel por %d." %(n, i))
            quant += 1
    return quant
while True:
    try:
        num = int(input("\nDigite um numero inteiro: "))
        while num <= 0:
            num = int(input("\nNúmero deve ser maior que 0. Digite novamneto!"))

        print("A quantidade de divisores de %d é %d." %(num, divisores(num)))
        break
    except:
        print('Valor inválido')
