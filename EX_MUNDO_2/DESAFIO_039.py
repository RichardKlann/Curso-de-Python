'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar no serviço militar
- Se é hora de ele se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

'''
idade = int(input('Informe a sua idade agora: '))

if idade < 18:
    print('Você deve de se alistar em {} ano(s).'.format(18-idade))
elif idade == 18:
    print('Você deve de se alistar neste ano!')
else:
    print('Você já deveria ter se alistado faz {} anos!'.format(idade - 18))
'''

from datetime import date

nascimento = int(input('Informe o ano do seu nascimento: '))

idade = date.today().year - nascimento

if idade < 18:
    print('Você deve de se alistar daqui a {} anos. Você ainda tem {} anos de idade!'.format(18 - idade, idade))
elif idade == 18:
    print('Você deve de se alistar NESTE ANO! Você já tem {} anos de idade!'.format(idade))
else:
    print('Você já deveria ter se alistado a {} ANOS ATRÁS! Você já tem {} anos de idade!'.format(idade - 18, idade))