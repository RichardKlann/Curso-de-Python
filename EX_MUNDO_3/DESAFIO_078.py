'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista
'''

valores = []
maiores = []
menores = []

for c in range (0, 5):
    entrada = int(input(f'Informe o valor da posição {c} da lista: '))
    valores.append(entrada)

maior = max(valores)
menor = min(valores)



'''
pos = 0
for valor in valores:
    if valor == max(valores):
        maiores.append(pos)
    if valor == min(valores):
        menores.append(pos)
    pos += 1
'''

print(f'\nA lista de valores digitados é: {valores}')

print(f'O maior valor digitado foi {maior} e está nas posições: ', end='')
for i, v in enumerate(valores):
    if maior == v:
        print(f'{i}... ', end='')

print('')
print(f'O menor valor digitado foi {menor} e está nas posições: ', end='')
for i, v in enumerate(valores):
    if menor == v:
        print(f'{i}... ', end='')

'''print(f'O maior valor digitado foi {max(valores)} e está nas posições: ', end='')
for c in maiores:
    print(f'{c}... ',end='')

print(f'\nO menor valor digitado foi {min(valores)} e está nas posições: ', end='')
for c in menores:
    print(f'{c}... ', end='')'''