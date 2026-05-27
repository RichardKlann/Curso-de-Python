'''
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro de uma lista e a segunda função, vai mostrar a soma entre todos os valores
pares sorteados dentro da função anterior.
'''
from random import randint
from time import sleep

#Funções
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    for i in range(0, 5, 1):
        num = randint(0, 10)
        lista.append(num)
        sleep(0.5)
        print(f'{num} ', end='', flush=True)


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {lista}, temos: {soma}')


#Programa principal
numeros = []
sorteia(numeros)
somaPar(numeros)