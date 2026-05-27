'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa dentro de um dicionário, e todos
os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) uma lista com todas as pessoas com idade acima da média
'''

pessoas = []
dados = {}
mulheres = []
idadeacima = []


while True:
    dados['nome'] = str(input('nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Masculino ou Feminino? [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F...')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    while True:
        cont=str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Digite somente S ou N...')
    if cont in 'N':
        break
   
qtdcadastro = len(pessoas)
print(f'A quantidade de pessoas cadastradas foram: {qtdcadastro}')

soma = 0
for i in range(0, len(pessoas)):
    soma += pessoas[i]['idade']
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i]['nome'][:])
    

media = soma/len(pessoas)
print(f'A média de idade do grupo é {media:.2f} anos')
print(f'Lista com todas as mulheres: {mulheres}')

for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        idadeacima.append(pessoas[i]['nome'][:])

print(f'Lista com todas as pessoas com idade acima da média {media:.2f}')
print(idadeacima)