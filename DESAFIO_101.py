'''
Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem o voto
NEGADO, OPCIONAL, OBRIGATÓRIO nas eleições.

até 18 anos - não vota
18 até 65 anos - obrigatório
acima de 65 anos - opcional
'''


#Funções
def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade <= 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa Principal
print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))