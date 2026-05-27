'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual o valor a ser sacado (número inteiro), e o programa vai informar quantas cédulas de cada valor
serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('=' * 30)
print('{:^30}'.format('BANCO RAK'))
print('=' * 30)

valor = int(input('Informe o valor que deseja sacar R$'))
ced = 50
qtdced = 0

while True:
    if valor >= ced:
        valor -= ced
        qtdced += 1
    else:
        if qtdced > 0:
            print(f'Total de {qtdced} cédulas de R${ced}')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qtdced = 0
        if valor == 0:
            break
print('=' * 30)












'''
print('=' * 30)
print('{:^30}'.format('BANCO RAK'))
print('=' * 30)
cedula50 = cedula20 = cedula10 = cedula1 = 0

valor = int(input('Qual o valor que você deseja sacar? R$'))

if valor/50 > 1:
    cedula50 = valor // 50
    valor -= (cedula50 * 50)

if valor/20 > 1:
    cedula20 = valor // 20
    valor -= cedula20 * 20

if valor / 10 > 1:
    cedula10 = valor // 10
    valor -= cedula10 * 10

if valor / 1 > 1:
    cedula1 = valor // 1
    valor -= cedula1

print(f'Total de {cedula50} cédulas de R$50')
print(f'Total de {cedula20} cédulas de R$20')
print(f'Total de {cedula10} cédulas de R$10')
print(f'Total de {cedula1} cédulas de R$1')
'''