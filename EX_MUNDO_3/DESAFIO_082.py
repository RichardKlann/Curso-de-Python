'''
Crie um programa que vai ler vários números e colocar uma lista.

Depois disso, crie duas listas extras que vão conter apenas valores pares e os valores ímpares digitados, respectivamente.

Ao final mostre o conteúdo das três listas geradas

Primeiro loop, apenas leia os valores e coloque na primeira lista. Depois avalie cada valor e gere as demais listas.
'''

lista1 = []     #Lista principal
lista2 = []     #Lista de números pares
lista3 = []     #Lista de números ímpares

while True:
    lista1.append(int(input('Digite um valor: ')))
    print(f'Número {lista1[-1]} foi adicionado com sucesso...')
    if input('Deseja continuar[S/N]? ').strip()[0] in 'Nn':
        break

for c in lista1:
    if c%2 == 0:
        lista2.append(c)
    else:
        lista3.append(c)

print(f'A lista principal digitada foi: {lista1}')
print(f'Todos os números pares da lista principal são: {lista2}')
print(f'Todos os números ímpares da lista principal são: {lista3}')