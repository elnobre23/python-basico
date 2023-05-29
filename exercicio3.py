nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

validador_nome = bool(nome)
validador_idade = bool(idade)

quantidade_letras = len(nome)

if validador_nome == 1 and validador_idade == 1:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome contém {quantidade_letras} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
    