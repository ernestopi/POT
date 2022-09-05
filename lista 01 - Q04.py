def media(nota1, nota2):
  media_notas = (nota1+nota2)/2
  if media_notas >= 6:
    return f'Parabéns! Você foi aprovado! sua média foi de {media_notas}'
  else:
    return f'Sua média foi {media_notas} voçe não foi aprovado.'

while True:
    try:
        nota1 = int(input("\nDigite a primeira nota: "))
        nota2 = int(input("\nDigite a segunda nota: "))
        while nota1 < 0:
            nota1 = int(input("\nNúmero deve ser maior que 0. Digite novamente!"))

        print(f'{media(nota1,nota2)}')
        break
    except:
        print('Valor inválido')