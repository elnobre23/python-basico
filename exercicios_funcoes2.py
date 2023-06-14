numero = int(input('Digite um número: '))

def par_ou_impar():
    
    if numero % 2 == 0:
        return f'O número {numero} é par'
    return f'O número {numero} é ímpar'

print(par_ou_impar())
