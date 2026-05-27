'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de 0 até 20.

Seu teclado deverá de ler um número pelo teclado (entre 0 e 20), e mostrá-lo por extenso.
'''

sequencia = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE',
             'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE',
              'DEZESSEIS', 'DESESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    num = -1
    while True:
        num = int(input('Informe um número entre 0 e 20: '))
        if num < 0 or num > 20:
            print('Digito inválido para o intervalo de 0 até 20...\n')
        else:
            break

    print(f'Você digitou o número {sequencia[num]}')
    print('Você digitou o número {}'.format(sequencia[num]))

    fim = str(input('Deseja finalizar o programa [S/N]: ')).strip().upper()[0]
    if fim in 'S':
        break
    print('')