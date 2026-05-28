'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randint
numjog = soma = cont = 0

while True:
    numjog = int(input('Informe um número: '))
    escolha = str(input('Impar ou Par [I/P]: ')).strip().upper()[0]
    numcpu = randint(0, 9)
    soma = numjog + numcpu
    print(f'O computador escolheu {numcpu}')
    print(f'A soma de ambos os números é: {soma}\n')
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    if resultado == escolha:
        cont += 1
        print('-' * 30)
        print('Parabéns, você acertou!')
        print('-' * 30)
    else:
        print('Uma pena, você perdeu...')
        break

print(f'\nVocê obteve {cont} vítórias consecutivas!')