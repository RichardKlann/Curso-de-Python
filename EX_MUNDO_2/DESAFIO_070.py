'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário quer continuar. No final, mostre:

a) Qual é o total gasto na compra?
b) Quantos produtos custam mais de R$1000?
c) Qual o nome do produto mais barato?
'''
print('=' * 30)
print('LOJÃO DO ENGENHEIRÃO')
print('=' * 30, '\n' )

soma = preco = cont1000 = precobarato = 0

while True:
    produto = str(input('Informe o nome do produto: R$'))
    preco = float(input(f'Informe o valor do produto {produto}: '))
    if preco > 1000:
        cont1000 += 1
    
    if precobarato == 0:
        precobarato = preco
        produtobarato = produto
    else:
        if preco < precobarato:
            precobarato = preco
            produtobarato = produto
    
    soma += preco

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    
    if continua in 'N':
        break
    print('=' * 30, end = '\n\n')

print('=' * 30)
print(f'O valor total da compra é R${soma:.2f}.')
print(f'A quantidade de produtos que custam mais que R$1000,00 é {cont1000}.')
print(f'O produto mais barato é {produtobarato} e o valor é R${precobarato:.2f}.')
