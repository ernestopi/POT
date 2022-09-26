
def criar_lista():
  lista = []
  for c in range(10):
    add = int(input())
    lista.append(add)
  return lista

ch1 = criar_lista()


def verificar(numero, ch1):
  for c in ch1:
    if numero == c:
      return True
    else:
      return False

y = int(input())
ch2 = verificar(y, ch1)
print(ch2)