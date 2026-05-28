'''Faça um programa que leia um número inteiro
 e mostre na tela o seu sucessor e antecessor
'''

n = int(input('Digite um número para que eu te entregue o antecessor e sucessor dele: '))
n_ant = n-1
n_suc = n+1
print('O número digitado foi {}, \nseu antecessor é {}, \nseu sucessor é {}'.format(n, n_ant, n_suc))