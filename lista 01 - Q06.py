def poligonos(lados, cm):
    if lados == 3 or lados == 4 or lados == 5:
        if lados == 3:
            perimetro = cm * 3
            print(f'O poligono informado é um TRIÂNGULO \nSeu perímetro é igual a {perimetro} centímetros')

        elif lados == 4:
            area = cm ** 2
            print(f'O poligono informado é um QUADRADO \nA área do quadrado é de {area:.1f}cm²')

        elif lados == 5:
            print('PENTÁGONO')

    else:
        print('Digite um valor válido')
    return lados

while True:
    try:
        lados = int(input("Digite o numero de lados.\n(Sendo 3 para trinagulo, 4 para quadrado e 5 para poligino): "))
        cm = float(input("\nDigite a medida dos lados: "))
        while lados != 3 and lados!= 4 and lados!= 5:
            lados = int(input("\nDigite o 3, 4 ou 5 para os lados: "))

        poligonos(lados,cm)
        break
    except:
        print('Valor inválido')
