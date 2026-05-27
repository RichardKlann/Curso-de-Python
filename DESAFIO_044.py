'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

valor_atual = float(input('Informe o valor atual do produto: R$'))
print('Informe o número da forma de pagamento: ')
print('1 - Dinheiro/Cheque')
print('2 - À vista no cartão')
print('3 - Cartão em até 2x')
forma_pagamento = int(input('4 - Cartão 3x ou mais\n'))

if forma_pagamento == 1:
    print('O valor a ser pago deve de ser R${:.2f}'.format(valor_atual*0.90))
elif forma_pagamento == 2:
    print('O valor a ser pago deve de ser R${:.2f}'.format(valor_atual*0.95))
elif    forma_pagamento == 3:
    print('O valor a ser pago deve de ser R${:.2f}'.format(valor_atual))
else:
    print('O valor a ser pago deve de ser R${:.2f}'.format(valor_atual*1.2))
