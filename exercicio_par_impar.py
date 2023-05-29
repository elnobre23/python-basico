numero = input('Digite um número inteiro: ')

if '.' in numero: #Verifica se o número digitado é inteiro ou não.
    print('Você não digitou um número inteiro.') #Havendo ponto flutuante na variável numero, o programa retorna uma mensagem
else: #Em não havendo ponto flutuante, o programa converte o valor em int.
    numero_inteiro = int(numero)
    verificador_par = numero_inteiro % 2
    if  verificador_par == 0: 
            print(f'O número {numero_inteiro} é par.')
    else:
            print(f'O número {numero_inteiro} é ímpar.')
