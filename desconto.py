preco_unitario = float(input('Insira o valor do preço unitário: '))
desconto1 = 0.1
desconto2 = 0.2
unidade = float(input('Insira a quantidade de unidades: '))
valor_desconto1 = (unidade * preco_unitario) * desconto1
valor_desconto2 = (unidade * preco_unitario) * desconto2
compra_1 = (preco_unitario * unidade) - valor_desconto1
compra_2 = (preco_unitario * unidade) - valor_desconto2
compra_3 = preco_unitario * unidade

if unidade > 20:
    print('O preço da sua compra foi de: R$ ', compra_2)
elif unidade > 10:
    print('O preço da sua compra foi de: R$ ', compra_1)
else:
    print('Não há descontos. O preço da sua compra foi de: R$ ', compra_3)
