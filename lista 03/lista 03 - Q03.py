def primo(numero):
  if type(numero) != str and type(numero) == int and numero > 0: 
    divisores = 0
    for c in range(1,numero+1):
        if numero%c == 0:
          divisores += 1
    if divisores == 2:
      return True
    else:
      return False
  else:
    return Exception

assert primo(83) == True
assert primo(1) == False
assert primo(17) == True
assert primo(2) == True
assert primo(13) == True
assert primo(4) == False
assert primo(1.2) == Exception
assert primo('!') == Exception
assert primo(6.7) == Exception
assert primo(0) == Exception
assert primo(True) == Exception
assert primo('Novecentos e 70') == Exception
print('Todos os testes estão OK!')