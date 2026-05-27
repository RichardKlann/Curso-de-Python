'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois mostre:

a) Quantos números foram digitados.
b) A lista de valores ordenadas de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = list()

while True:
    numeros.append(int(input('Digite um número: ')))
    loop = input('Deseja continua [S/N]: ').strip()[0]
    if loop in 'Nn':
        break

print()
print(f'A quantidade de números digitados foi {len(numeros)}...')

numeros.sort(reverse=True)
print(f'A lista toda de forma decrescente é: {numeros}')

if 5 in numeros:
    print('O valor 5 está dentro da lista...')
else:
    print('O valor 5 não está dentro da lista...')
