
def segundos_para_horas(quant_segundos):
    if type(quant_segundos) == str or quant_segundos <= 0:
        return Exception
    else:
        horas = quant_segundos//3600
        resto = quant_segundos%3600
        minutos = resto//60
        segundos = resto%60
        return horas, minutos, segundos


assert segundos_para_horas(95) == (0,1,35)
assert segundos_para_horas(-10) == Exception
assert segundos_para_horas(0) == Exception
print("Todos os teste ok!")