i = 0
contador = 0.0
soma = 0.0
media = 0.0
x = 0.0

print('Quantos elementos terá o vetor? ')
n = int(input())

pares = [0.0] * n
impares = [0.0] * n

for i in range(0, n):
    print('Digite um número: ')
    x = float(input())
    if x % 2 == 0:
        pares[i] = x
    else:
        impares[i] = x

for i in range(0, n):
    if pares[i] != 0:
        contador += 1

for i in range(0, n):
    soma += pares[i]

if soma == 0:
    print('Nenhum número par')
else:
    media = soma / contador
    print(f'Média dos pares: ', format(media, '.1f'))
