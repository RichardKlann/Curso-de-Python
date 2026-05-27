#AULA 06 - TIPOS PRIMITIVOS E SAÍDA DE DADOS
'''
Para ver o tipo primitivo de uma variável:
print(type(variável))


Para converter uma variável de um tipo primitivo para outra:
int(variável) -> converte para um valor inteiro (se possível)
float(variável) -> converte para um ponto flutuante (se possível)
str(variável) -> converte para uma string (todas as leituras do teclado são transformadas em str por padrão)
bool(variável) -> converte para uma condição de "binário", True ou False (se possível)


Ao colocar print(variável.is...)
print(variável.isalnum) - printa se é alfanumérico
print(variável.isnum) - printa se é numerico
Existem N situações que podem ser avaliadas pelo variável.is...
'''




#AULA 07 - OPERADORES ARITIMÉTICOS
'''
+   Adição
-   Subtração
*   Multiplicação
/   Divisão
**  Potência
//  Divisão inteira
%   Resto da divisão]

Ordem de Precedência
1°  ()
2°  **
3°  *   /   //  %
4°  +   -
'''




#AULA 08 - UTILIZANDO MÓDULOS
'''
Aprendemos a importar bibliotecas: comando
import math (para importar a biblioteca math)
from math import sqrt (para poupar memória, esta é a sintaxe para que possamos importar apenas um comando da biblioteca)

'''
'''
from math import ceil, sqrt
num = float(input('Informe um número: '))
raiz = sqrt(num)
print ('A raiz quadrada de {:.0f} é {:.0f}'.format(num, ceil(raiz)))
'''



#DESAFIO 19
'''
lista = [n1, n2, n3, n...] - Serve para criar uma lista, ou um vetor em programação
'''



#AULA 09 - MANIPULAÇÃO DE STRING
'''
frase[x:y:z]
x - indica o início que quero utilizar da string (posição da letra começando em 0)
y - indica o final da string que quero utilizar (posição da letra terminando no infinito)
z - indica a quantidade de letras que quero que pule, a partir da letra inicial

C   U   R   S   O       E   M       V   I   D   E   O       P   Y   T   H   O   N   
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20

Frase[2:5:1] = RS (APENAS ESSAS LETRAS SERÃO IMPRESSAS)

PRIMEIRA FUNÇÃO: len (significa lenght - comprimento)
len(frase) - Irá mostrar qual o comprimento da frase - a frase acima seriam 21 caracteres

SEGUNDA FUNÇÃO 
frase.count('o') - Conta quantas vezes a letra o minúsculo aparece dentro da variável
frase.count('o', 0, 13) - Conta quantas vezes a letra o minúsculo aparece com o fatiamento de 0 à 13
frase.find('deo') - localiza onde inicia a sequência 'deo' dentro da string - ex inicia em 11
frase.find('Android') - Neste exemplo como ele não encontrou nada, retornará -1
'curso' in frase - É uma pergunta: Existe a palavra 'curso' na variável frase? True or False

TRANSFORMAÇÃO
frase.replace('Python', 'Android') - substituir onde está a palavra Python por Android
frase.upper() - Tudo o que é minúsculo na string ele troca para maiúsculo
frase.lower() - Tudo o que é maiúsculo na string ele troca para minúsculo
frase.capitalize() - Todos os caracteres vão para minúsculo, e apenas o primeiro caractere da string toda é maiúsculo
frase.title() - Analisar quantas palavras tem na string, e vai deixar maiúsculo todos os primeiros caracteres das palavras

ex2
            A   p   r   e   n   d   a       P   y   t   h   o   n  
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18

frase.strip() - Remove todos os espaços inúteis dentro da variável - 1,2,3,17,18 são removidos
frase.rstrip() - Igual ao anterior, porém apenas remove os espaços inúteis da parte da direita da variável
frase.lstrip() - Igual ao anterior, porém apenas remove os espaços inúteis da parte da esquerda da variável


frase.split() - Irá ocorrer uma divisão dentro da string, considerando os espaços - Gera uma nova lista com uma nova cadeia de caracteres

'-'.join(frase) - Irá juntar a cadeia da lista da string.split(), e vai adicionar um tracinho em cada divisão onde era para ser o espaço


print("""COLOQUE UM TEXTO GRANDE""") - Vai ser escrito o texto todo

#frase = 'Curso em Vídeo Python'
#dividido = frase.split
#print(dividido[2] [3])
[2] - irá selecionar apenas a palavra Vídeo para printar
[3] - irá printar somente o quarto caractere da palavra antes escolhida
'''




#FORMATAÇÃO DE STRINGS
'''
1 - F STRINGS:
nome = "Richard"
idade = 30

print(f"Meu nome é {nome} e tenho {idade} anos")



2 - FORMATAÇÃO DE NÚMEROS: 
valor = 1234.5678

print(f"{valor:.2f}")   # 2 casas decimais → 1234.57
print(f"{valor:10.2f}") # largura 10


3 - ALINHAMENTO: (MUITO USADO EM TABELAS)
texto = "Python"

print(f"{texto:<10}")  # esquerda
print(f"{texto:>10}")  # direita
print(f"{texto:^10}")  # centralizado



4 - PRRENCHIMENTO COM CARACTERES: 
print(f"{'42':0>5}")  # 00042
print(f"{'42':*<5}")  # 42***



5 - FORMATAÇÃO MONETÁRIA:
preco = 1234.5

print(f"R$ {preco:,.2f}")



6 - PORCENTAGEM:
taxa = 0.85

print(f"{taxa:.2%}")  # 85.00%



7 - FORMATAÇÃO PARA TABELAS: 
nome = "Ana"
idade = 25
cidade = "Navegantes"

print(f"{nome:<10} | {idade:^5} | {cidade:<15}")



8 - FORMATANDO DENTRO DE LOOPS:

dados = [("Ana", 25), ("João", 30)]

for nome, idade in dados:
    print(f"{nome:<10} | {idade:>3}")

    
'''





#AULA 10 - CONDIÇÕES (PARTE 1)
'''
if carro.esquerda(): #identação para condicional se

else: #Identação para condicional senão.

tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3:
    print('Seu carro é novo.')

else:
    print('Seu carro está velho.')
print('--FIM--')

#Condição simplificada do mesmo programa acima

tempo = int(input('Quantos anos tem seu carro: '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')
'''
'''
nome = str(input('Informe o seu nome: '))
if nome == 'Richard':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))
'''

'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 7:
    print('Ops, você foi reprovado!')

else:
    print('Parabéns, você foi aprovado!')
'''






#AULA 11 - CORES NO TERMINAL
'''
ANSI - escape sequence

\033[STYLE; TEXT; BACKm
\033[0;33;44m

STYLE - Indica o estilo da fonte - normal, negrito, sublinhada...
TEXT - Qual a cor do texto
BACK - Qual a cor do background (ambiente)

STYLE
0 - none
1 - negrito
4 - sublinhado (underline)
7 - negativo (o que é fundo vai pra letra e o que vai para letra vira fundo)

TEXT        BACK
30          40        Branco
31          41        Vermelho
32          42        Verde
33          43        Amarelo
34          44        Azul
35          45        Magenta
36          46        Ciano
37          47        Cinza
'''
'''
Método para criar as cores mais fácil e depois apenas substituir (Criar um dicionário)

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m' }

Utilização:
cores['pretoebranco']
'''
print('\033[0;31;42mOlá Mundo!')
print('\033[1;32;43mOlá Mundo!')
print('\033[4;33;44mOlá Mundo!')
print('\033[7;35;46mOlá Mundo!')
print('Olá olá olá')