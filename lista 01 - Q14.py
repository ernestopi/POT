def fatorial(n):
  fatorial = 1
  for c in range(n,0,-1):     # n = start; 0 = stop; -1 = step.
    fatorial *= c
  return fatorial


def resultado(numero):
  S = 1
  for c in range(1, numero+1):
    S += 1/fatorial(c)
  return S.__round__(3)

while True:
  try:
    numero = int(input('DIGITE NUMERO INTEIRO E POSITIVO '))
    if numero > 0:
      print(resultado(numero))
      break
      while numero <= 0:
          numero = int(input())
          if numero > 0:
              print(resultado(numero))
              break

  except:
    print('DIGITE VALOR INTEIRO E POSITIVO')