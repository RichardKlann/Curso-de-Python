'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços.
(Pode ser de frente para trás, ou de trás para frente que vai dar a mesma coisa)
ex: APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

initial_phrase = str(input('Escreva uma frase: '))

initial_phrase = initial_phrase.strip().upper() #Remover os espaços desnecessários

phrase_divided = initial_phrase.split() #Transforma cada palavra em um item dentro do vetor
phrase_without_spaces = ''.join(phrase_divided) #Junta todas as palavras sem espaços entre elas
inv_phrase_without_spaces = phrase_without_spaces[::-1]

print(phrase_without_spaces)
print(inv_phrase_without_spaces)

if phrase_without_spaces == inv_phrase_without_spaces:
    print('A frase digitada é um PALÍNDROMO')
else:
    print('A frase digitada acima não é um palíndromo')