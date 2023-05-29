primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

intvalor1 = int(primeiro_valor)
intvalor2 = int(segundo_valor)

if intvalor1 > intvalor2:
    print(f'{intvalor1} é maior do que {intvalor2}.')
elif intvalor2 > intvalor1:
    print(f'{intvalor2} é maior do que {intvalor1}.')
else:
    print(f'{intvalor1} é igual a {intvalor2}.')
