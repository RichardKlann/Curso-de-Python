'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''

idade = contidade = conth = contm = 0

while True: 
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo masculino ou feminino [M/F]: ')).strip().upper()[0]
    if sexo in 'M':
        conth += 1

    idade = int(input('Digite a idade em anos: '))
    if idade > 18:
        contidade += 1

    if sexo in 'F' and idade < 20:
        contm += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    print('=' * 40)
    if continua in 'N':
        break

print(f'a) {contidade} pessoas tem mais de 18 anos.')
print(f'b) {conth} homens foram cadastrados.')
print(f'c) {contm} mulheres com menos de 20 anos foram cadastradas.')