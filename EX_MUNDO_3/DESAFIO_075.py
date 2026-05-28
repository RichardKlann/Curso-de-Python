'''
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
'''

tupla = (int(input('Digite um número: ' )), 
         int(input('Digite outro número: ' )),
         int(input('Digite mais um número: ' )),
         int(input('Digite o último número: ')))

print(tupla)

cont9 = tupla.count(9)
print(f'a) O valor 9 apareceu {cont9}')

if 3 in tupla:
    posi3 = tupla.index(3)
    print(f'b) O valor 3 está na posição {posi3}')
else:
    print('b) Não possui nenhum valor 3 na tupla')

print('c) Os valores pares digitados foram: ', end = '')

for n in tupla:
    if n % 2 == 0:
        print(n, end = ' ')


