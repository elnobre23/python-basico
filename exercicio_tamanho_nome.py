nome = input('Digite seu primeiro nome: ')
tamanho_do_nome = len(nome) #Utilizando a função len, obtenho a quantidade de letras no nome e armazeno numa variável.

if tamanho_do_nome <= 4:
    print('Seu nome é curto.')
elif tamanho_do_nome > 6:
    print('Seu nome é muito grande')
else:
    print('Seu nome é normal')
    