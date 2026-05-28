'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, e a quantida de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e 
R$0,15 por Km rodado.'''

dias = int(input('Informe a quantidade de dias que o carro ficou alugado: '))
km = float(input('Informe a quantidade total de Km rodados: '))

print('Considerando que o carro foi alugado por: \n {} dias, e que teve {:.1f}Km rodados'.format(dias, km))
print('O valor total da locação será: R${:.2f}'.format(dias*60+km*0.15))