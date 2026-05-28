'''
Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas,
ainda não atingiram a maioridade, e quantas já são maiores (considerar 21 anos para maioridade)
'''
from datetime import date

ano_atual = date.today().year
menor = maior = 0

for c in range (1, 8, 1):
    ano = int(input('Informe o ano de nascimento da pessoa n° {}: '.format(c)))
    if ano_atual - ano < 21:
        menor = menor + 1
    else:
        maior = maior + 1

print('Considerando todos os anos informados, temos {} menores de 21 anos e {} com 21 ou mais anos.'.format(menor, maior))















'''from datetime import date

atual = date.today().year
maior = menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print ('De todas o anos digitados, {} ainda não atigiram a maioridade e {} já atingiram a maioridade.'.format(menor, maior))'''