'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar de 80 Km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite
'''

limite = 80
velocidade = int(input('Qual a velocidade do carro? '))


if velocidade <= limite:
    print('Tenha um bom dia! Dirija com segurança')

else:
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(limite))
    print('Você deve pagar uma multa de R${:.2f}!'.format(float((velocidade - limite)*7)))
    print('Tenha um bom dia! Dirija com segurnça!')
