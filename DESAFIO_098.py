'''
Faça um programa que tenha uma função chamada contador(),
que receba 3 parâmetros: início, fim, passo e realize a contagem.

Seu programa tem que realizar 3 contagens através da função criada:

a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
'''
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1
        
    print('=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio <= fim:
        num = inicio
        while num <= fim:
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
            num += passo
        print()
    if inicio >= fim:
        num = inicio
        while num > fim:
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
            num -= passo
        print()
    print('=' * 20)

contador(0, 10, 1)
contador(10, 0, 2)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)