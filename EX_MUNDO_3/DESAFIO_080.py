'''
Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de
inserção (sem usar o sort()).

No final mostre a lista ordenada na tela.
'''

valores = []

for c in range(0,5):
    num = int(input('Digite um valor: '))

    if c == 0:
        valores.append(num)
        print('Valor adicionado no final da lista...')
    elif num > max(valores):
        valores.append(num)
        print('Valor adicionado no final da lista...')
    else: 
        pos = 0
        while pos < len(valores):
            if num < valores[pos]:
                valores.insert(pos, num)
                print('Valor adicionado na posição {}'.format(pos))
                break
            pos += 1
    
print(valores)