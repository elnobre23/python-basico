nome = input('Qual é seu nome? ')
altura = float(input('Qual é sua altura em metros? '))
peso = float(input('Qual é seu peso? '))
imc = peso / (altura * altura)

print(f'O IMC de {nome} é {imc:.2f}')
