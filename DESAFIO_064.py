'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 
usuário digitar 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)
'''

print('Informe vários números inteiros. No final irei mostrar a soma de todos eles + quantos números você me informou!')
print('OBS: Caso desejar parar, digite "999".')

cont = 1
resultado = 0
n = 0
while n != 999:
    valor = int(input('Número {}: '.format(cont)))
    cont +=1
    resultado += valor
    n = valor

n -= 1
resultado -= valor
print('Você digitou {} números para somar, e o resultado foi {}'.format(cont, resultado))
