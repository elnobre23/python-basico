def multiplicador(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

resultado = multiplicador(1*2*3*4*5)
print(resultado)
