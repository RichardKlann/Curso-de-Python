'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso você deve de mostrar, para cada palavra, quais são as suas vogais.
'''

tupla = ('AMANHA', 'NOVIDADE', 'SUSANA', 'RICHARD', 'ASTRONAUTA', 'AGROPECUARIA')

for palavra in tupla:
    print(f'Na palavra {palavra.upper()} temos essas vogais: ', end='')
    for letra in palavra:
        if letra in 'aAeEiIoOuU':
            print(letra, end=' ')
    print('')
        


'''
tamtupla = len(tupla)

for c in range (0, tamtupla):
    tampal = len(tupla[c])
    for l in range (0, tampal):
        if l == 0:
            print(f'Na palavra {tupla[c].upper()} temos as vogais: ', end = '')

        if tupla[c][l] in 'AaEeIiOoUu':
            print (tupla[c][l], end = ' ')
        
        
        if l+1 == tampal:
            print('')
'''