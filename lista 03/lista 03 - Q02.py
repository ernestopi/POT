def calcula_media(n1, n2, n3, letra):
    if type(n1) != int and type(n1) != float:
        return Exception
    if type(n2) != int and type(n2) != float:
        return Exception
    if type(n3) != int and type(n3) != float:
        return Exception
    if n1 < 0 or n2 < 0 or n3 < 0 or n1 > 10 or n2 > 10 or n3 > 10:
        return Exception
    if letra not in ('A', 'P'):
        return Exception

    if letra == 'A':
        return round((n1 + n2 + n3) / 3, 1)

    return round((n1 * 5 + n2 * 3 + n3 * 2) / 10, 1)


assert calcula_media(7, 6.5, 8, 'A') == 7.2
assert calcula_media(7, 5, 4.5, 'P') == 5.9
assert calcula_media('a', 'a', 'a', 'A') == Exception
assert calcula_media(7, 6.5, 8, 'F') == Exception
assert calcula_media(1, 6.5, 11, 'F') == Exception
assert calcula_media(-1, 11, 8.5, 'G') == Exception
print("Todos os teste ok!")


