def peso_ideal(altura, sexo):
  if sexo == 1:
    mulher = (62.1*altura) - 44.7
    return mulher.__round__(2)

  elif sexo == 2:
    homem = (72.7*altura) - 58
    return homem.__round__(2)

while True:
    try:
        sexo = int(input("Digite o sexo, (1 para sexo Feminino e 2 para masculino): "))
        altura = float(input("\nDigite sua altura: "))
        while sexo != 1 and sexo!= 2:
            sexo = int(input("\nDigite o 1 ou 2 para o sexo: "))
            altura = float(input("Insira um valor correto para altura: "))

        print(f'O seu peso ideal é {peso_ideal(altura,sexo)}kg.')
        break
    except:
        print('Valor inválido')
