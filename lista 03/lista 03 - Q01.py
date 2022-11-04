
def volume_esfera(raio):
    if type(raio) == str or  type (raio) == bool or raio <= 0:
        return Exception
    return round(4/3 * 3.14 * raio**3, 2)

assert volume_esfera(-1) == Exception
assert volume_esfera('abc') == Exception
assert volume_esfera('*') == Exception
assert volume_esfera(True) == Exception
assert volume_esfera(False) == Exception
assert volume_esfera(1.0) == 4.19
assert volume_esfera(1) == 4.19
assert volume_esfera(10) == 4186.67
assert volume_esfera('$') == Exception
assert volume_esfera('@') == Exception
print("Todos os testes estão ok!")
