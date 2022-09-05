def celsius_func(temperatura_fah):
  celsius = ((temperatura_fah-32)/9)*5
  return celsius.__round__(4)

while True:
  try:
    temperatura_fah = float(input('Insira um valor para temperatura em Fahrenheit: '))
    print(f'A temperatura de {temperatura_fah}ºF equivale a {celsius_func(temperatura_fah)}ºC')
    break
  except:
    print('Temperatura inválida! Tente novamente!')
    