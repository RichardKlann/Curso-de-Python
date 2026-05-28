'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

print('=' * 20 + ' CALCULADORA SIMPLIFICADA ' + '=' * 20)
valor1 = valor2 = ''
novosnumeros = True
fim = True

while fim != False:
    while novosnumeros == True:
        while valor1 == '':
            valor1 = input('\nDigite o primeiro número: ')
            try:
                valor1 = float(valor1)
            except ValueError:
                print('\nDigite um número válido!\n')
                valor1 = ''

        while valor2 == '':
            valor2 = input('Digite o segundo número: ')
            try:
                valor2 = float(valor2)
                novosnumeros = False
            except ValueError:
                print('Digite um número válido!\n')
                valor2 = ''

    while novosnumeros == False:
        print("""\nAbaixo você verá o menu de opções de operação da calculadora: 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
        operacao = input('\nInforme o número da opção desejada: ')
        try:
            operacao = int(operacao)
            if operacao == 1:
                resultado = valor1 + valor2
                print('\nO resultado de {:.2f} + {:.2f} = {:.2f}'.format(valor1, valor2, resultado))
            elif operacao == 2:
                resultado = valor1 * valor2
                print('\nO resultado de {:.2f} * {:.2f} = {:.2f}'.format(valor1, valor2, resultado))
            elif operacao == 3:
                if valor1 == valor2:
                    print('\nOs valores digitados são iguais!')
                if valor1 != valor2:
                    if valor1 > valor2:
                        resultado = valor1
                    elif valor2 > valor1:
                        resultado = valor2
                    print('\nO valor maior é: {:.2f}'.format(resultado))
            elif operacao == 4:
                novosnumeros = True
                valor1 = ''
                valor2 = ''
                break
            elif operacao == 5:
                fim = False
                break
            else:
                print('\nOPÇÃO INVÁLIDA! DIGITE NOVAMENTE...')
        except ValueError:
            print('\n\nOPÇÃO INVÁLIDA! SOMENTE NÚMEROS...\n\n')
