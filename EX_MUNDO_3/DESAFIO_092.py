'''
Crie um programa que leia o nome, ano de nascimento, e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, quantos anos a pessoa vai se 
aposentar. (considerar 35 anos de contribuição para se aposentar)
'''
from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CTPS (caso não tiver digite 0): '))
if dados['ctps'] != 0:
    dados['ano contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['ano contratação'] + dados['idade'] + 35 - datetime.now().year

print('=-' *30)

for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
