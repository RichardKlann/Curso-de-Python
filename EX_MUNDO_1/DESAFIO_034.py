'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00 calcule um aumento de 10%

Para salários inferiores ou iguais, o aumento será de 15%
'''

salarioAtual = float(input('Me informe o seu salário atual: '))

if salarioAtual <= 1250:
    taxa = 1.15
else:
    taxa = 1.10

salarioAjustado = salarioAtual * taxa

print('Parabéns, você ganhou uma promoção! Seu salário reajustou {:.0f}%'.format((taxa-1)*100))
print('A partir de agora seu salario que era R${:.2f} passa a ser R${:.2f}'.format(salarioAtual, salarioAjustado))