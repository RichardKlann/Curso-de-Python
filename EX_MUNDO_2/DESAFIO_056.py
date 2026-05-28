'''
Desenvolva um programa que leia:
nome
idade
sexo
de 4 pessoas.
No final mostre:
1 - A média de idade do grupo.
2 - Qual o nome do homem mais velho.
3 - Quantas mulheres tem menos de 20 anos. 
'''


idade = idade_total = idade_h_mais_velho = qtd_mulheres_menor_20_anos = 0
nome_h_mais_velho = ''

for c in range (1, 5, 1):
    nome = str(input('Digite o nome da pessoa n°{}: '.format(c))).upper().strip()
    idade = int(input('Digite a idade da pessoa n°{}: '.format(c)))
    sexo = str(input('Digite o sexo M para masculino e F para feminino da pessoa n° {}: '.format(c))).upper().strip()
    print('')
    if nome_h_mais_velho == '' and sexo == 'M':
        nome_h_mais_velho = nome
        idade_h_mais_velho = idade
        idade_total = idade
    elif idade > idade_h_mais_velho and sexo == 'M':
        idade_h_mais_velho = idade
        nome_h_mais_velho = nome
        idade_total += idade
    elif sexo == 'F' and idade < 20:
        qtd_mulheres_menor_20_anos += 1
        idade_total += idade

    
media_idade = idade_total/4
print('A média de idade é {}.'.format(media_idade))
print('O nome do homem mais velho é {}.'.format(nome_h_mais_velho))
print('Número de mulheres com menos de 20 anos é {}.'.format(qtd_mulheres_menor_20_anos))
