'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base
da conversão:

1 - para binário
2 - para octal
3 - para hexadecimal
'''

numero = int(input('Informe um número qualquer: '))
operacao = int(input('''Informe o número da operação operação que deseja realizar:
1 - Converter número para Binário
2 - Converter número para Octal
3 - Converter número para Hexadecimal\n'''))

if operacao == 1:
    print('O número {} convertido para binário é representado por: {}'.format(numero, bin(numero)))
elif operacao == 2:
    print('O número {} convertido para Octal é representado por: {}'.format(numero, oct(numero)))
elif operacao == 3:
    print('O número {} convertido para hexadecimal é representado por {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('Opção inválida. Tente novamente!')