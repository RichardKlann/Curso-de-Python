'''
Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de 3, e que se
encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A sequência teve {} vezes somadas, e o total da soma dos números entre 1 e 500 divisíveis por 3 foi {}'.format(cont, soma))
