'''
Escreva um programa para aprovar o empréstimo bancário para aprovar a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar.

Calcule o valor mensal da prestação. Sabendo que ela não pode exceder 30% do salário
Ou então o empréstimo será negado
'''

#Entrada de dados
valor_casa = float(input('Informe o valor da casa que deseja comprar: R$'))
salario = float(input('Informe o valor do seu salário atual: R$'))
anos = float(input('Informe em quantos anos você deseja quitar a casa: '))

meses = anos*12
valor_parcela = valor_casa/meses

if valor_parcela > salario*0.30:
    print('''Infelizmente seu empréstimo não pode ser aprovado.
 O valor da parcela mensal excede 30% do valor do seu salário.''')
else:
    print('Parabéns! Você acaba de ter seu empréstimo aprovado.')
    print('O valor da parcela do seu financiamento será de R${:.2f} em {:.0f} vezes!'.format(valor_parcela, meses))