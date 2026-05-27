'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela. 7 ou mais é aprovado, abaixo de 7 reprovado.
'''
ficha = {}

ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Qual a média de {ficha["nome"]}: '))

if ficha['media'] >= 7:
    ficha['situacao'] = 'Aprovado'
elif ficha['media'] >= 5:
    ficha['situacao'] = 'Recuperação'
else:
    ficha['situacao'] = 'Reprovado'

print('=-' * 30)
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')
