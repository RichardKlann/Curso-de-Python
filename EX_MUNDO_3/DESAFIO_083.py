'''
Crie um programa onde o usuário crie uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a
expressão passada está com o parenteses abertos e fechados na ordem correta.
'''
expressao = []

valor = str(input('Digite uma expressão: '))

for c in valor:
    if c == '(':
        expressao.append(c)
    elif c == ')':
        expressao.pop()

if len(expressao) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')