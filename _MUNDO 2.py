#AULA 12 - CONDIÇÕES ANINHADAS
'''
IF - se
ELSE - então
ELIF - então se (condicional dentro da outra)

exemplo aula
nome = str(input('Qual é o seu nome?'))

if nome == 'Gustavo':
    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')

elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino')
    
else: 
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))
'''






#AULA 13 - ESTRUTURA DE REPETIÇÃO FOR
'''
LAÇOS DE REPETIÇÃO - PARTE 1

for c in range(1,10): - Para 'c' dentro do range entre 1 e 10 execute:

for c in range(1,10):
    passo
    pula
passo
pega


for c in range(0,3):
    print(c)

for c in range(6, 0, -1): Ele faz a contagem diminuindo 1 unidade    

inicio = int(input('Digite o INÍCIO da repetição: '))
fim = int(input('Digite o FIM da repetição: '))
passo = int(input('Digite o PASSO da repetição: ))

for c in range(inicio, fim, passo):

s = s + n #é a mesma coisa que 
s += n (é omitido o S quando se coloca o sinal na frente do igual)
'''

#Para não pular linha print = ('alguma coisa', end = ' ')


#AULA 14 - ESTRUTURA DE REPETIÇÃO WHILE
'''
O comando FOR é utilizando quando eu sei o número de passos, ou qual o limite que vai ser chego.
É um loop de repetição com variável de controle.

O comando WHILE é utilizado quando não sei quantos passos eu vou realizar para atingir o objetivo.
É um loop de repetição com teste lógico.

Exemplo para o mesmo programa:
for c in range (1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
'''


#AULA 15 - INTERROMPENDO REPETIÇÕES WHILE
'''
Comando interrompa = break

PEP do python das F STRINGS - O similar ao .format, pode escrever desta forma: 

print(f'O {nome} tem {idade}.')

Sendo nome e idade duas variáveis.
'''