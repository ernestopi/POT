numeroz = []

for c in range(5):
  y = int(input())
  numeroz.append(y)

def inverso(numeroz):
  lista_inversa = []
  for d in numeroz:
    lista_inversa.insert(0,d)
  return lista_inversa

ch = inverso(numeroz)
print(ch)

