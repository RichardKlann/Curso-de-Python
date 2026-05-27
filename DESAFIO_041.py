'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SENIOR
- acima: MASTER
'''

from datetime import date

ano_nascimento = int(input('Informe o ano do seu nascimento: '))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade > 19 and idade <=20:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')