'''
Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, mas agora 
usando o laço for.
'''

numero = int(input('Digite um número e tenha a sua tabuada: '))

for c in range (1, 11, 1):
    print (f'{numero} x {c:2} = {numero*c}')