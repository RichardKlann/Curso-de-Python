''''Faça um algoritmo que leia o salário de um funcionario
e mostre seu novo salário com 15% de aumento'''

sal_atual = float(input('Me informe o seu salário atual: '))
print('Parabéns, você teve uma promoção! O seu salário atual passa a ser: R${:.2f}'.format(sal_atual*1.15))