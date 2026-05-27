'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
de cada aluno individualmente.

Flag para finalizar o programa usuário digitar 999

'''

ficha = []
aux = []

id = 1
while True:
    nome = str(input('Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    if input('Deseja continuar [S/N]: ').strip()[0] in 'Nn':
        break

print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 26)

while True:
    id = int(input('Deseja ver as notas de qual aluno? (999 interrompe): '))
    if id == 999:
        break
    print(f'Notas de {ficha[id][0]} são: {ficha[id][1]}')
    print('----------------------------------------')