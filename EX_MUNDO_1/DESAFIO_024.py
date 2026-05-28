'''Crie um programa que leia o nome da sua cidade e diga se ela começa ou não com o nome 'SANTO' 
'''

cidade = str(input('Digite o nome da sua cidade: '))
cidade = cidade.strip()
cidade = cidade.upper()
divisao = cidade.split()
print(divisao)
print('SANTO' in divisao[0])