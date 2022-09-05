def max(a, b):
  maior = -99999
  if a > maior and a > b:
    maior = a
    return maior

  elif b > maior and b > a:
    maior = b
    return b

  elif a == b:
    return a or b



for c in range(5):
  y, x = input().split(" ")
  y = int(y)
  x = int(x)
  ch = max(y,x)
  print(ch)