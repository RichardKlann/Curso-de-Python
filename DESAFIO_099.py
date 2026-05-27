'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior. 
'''
from time import sleep

def maior(*num):
    print('-=' * 40)
    print('Analisando os valores passados...')
    cont = ma = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            ma = valor
        else:
            if valor > ma:
                ma = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi: {ma}')
    print('-=' * 40)

maior(1, 2, 4, 5, 90, 34, 3, 100)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()