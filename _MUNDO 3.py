#AULA 16 - TUPLAS
'''
VARIÁVEIS COMPOSTAS - TUPLAS

Até agora foram utilizadas apenas variáveis simples, ou seja, que apenas armazena um dado em uma memória. Possui apenas um espaço
para armazenar dados.

Porém é possível adicionar quantos espaços quiser dentro de uma mesma variável. Que pode ser feito por meio de Tuplas.

print(lanche[0]) - mostra o elemento 0 da variável lanche.
print(lanche[0:2]) - mostra os elementos 0 e 1, excluindo o número 2 da variável lanche.
print(lanche[1:]) - mostra o elemendo 1 e todos os próximos até o último.
print(lanche[-1]) - mostra o último elemento. se for 4, o -1 é o 4.

funciona a função len. exemplo: len(lanche) = 4 (se tiver 4 espaços na memória.)

for c in lanche:
    print(c)

'AS TUPLAS SÃO IMUTÁVEIS!


SINTAXE: 

lanche = ('HAMBURGUER', 'SUCO', 'PIZZA', 'PUDIM')
lanche[1] = SUCO
lanche[-2] = PIZZA
lanche[1:3] = ('SUCO', 'PIZZA')


3 FORMAS DE MOSTRAR OS ELEMENTOS DA TUPLA
for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print(sorted(lanche)) - Vai mostrar a tupla em ordem alfabética (apenas mostrar, não mudou a variável.)




a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b -> resultado: c = (2, 5, 4, 5, 8, 1, 2)

print(c.count(5)) - conta quantas vezes aparece o número 5 dentro da tupla C
print(c.index(8)) - Em qual posição está o 8
print(c.index(5, 1)) - Em qual posição está o 5 após a posição 1




pessoa = ('Gustavo', 39, 'M', 99.88) - Posso ter dados de qualquer tipo dentro de uma tupla
print(pessoa)

del(pessoa) - posso apagar uma tupla (única coisa possível)

'''





#AULA 17 - VARIÁVEIS COMPOSTAS - LISTAS (PARTE 1)
'''
MUITO SIMILAR AS TUPLAS, PORÉM AS LISTAS PODEM SER MODIFICADAS.

aqui eu posso por exemplo dar o seguinte comando
lanche[3] = 'picolé' - por mais que tivesse outra coisa, eu posso modificar.


- CRIAR LISTAS: para criar as listas ao invés de usar parenteses, é utilizado colchetes!
lista = ['estou', 'criando', 'a', 'primeira', 'lista']


valores = list(range(4,11)) - irá criar uma lista com valores que vão de 4 até 11.(último não conta) Como abaixo:
valores = [4, 5, 6, 7, 8, 9, 10]


- ADICIONAR OBJETOS:
posso adicionar novos itens dentro da minha lista já criada utilizando o comando append:
lanche.append('biscoito')

adicionar outro objeto dentro da lista, dizendo em qual posição, e ele irá movimentar para a direita todos os indices
lanche.insert(posição que quero adicionar, 'objeto a ser adicionado')
lanche.insert(0, 'biscoito)

- DELETAR OBJETOS:
del lanche[3] - remove o objeto do lanche na posição 3
lanche.pop(3) - remover o objeto do lanche na posição indicada
lanche.remove('Pizza') - eliminar o objeto pelo conteúdo.

Todos estes meios de deletar irão remanejar os índices da lista. Deletando ele não deixa uma posição 'vazia'

Se eu tentar remover um objeto que não está na lista, irá dar um erro na programação. Para contornar isso, usar:
    if 'pizza' in lanche:
        lanche.remove('pizza')

        
DEIXAR O OBJETO ORDENADO
valores.sort() - Ordem crescente
valores.sort(reverse=True) - Ordem decrescente


ENCONTRAR AS POSIÇÕES DOS VALORES DENTRO DA LISTA
for i, v, in enumerate(valores):        i é o índice (posição) v é o valor em si
    print(f'Na posição {i} encontrei o valor {v}!')
print('Cheguei no final da lista')


ex:
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))



AO IGUALAR UMA LISTA COM A OUTRA
a = [1, 2, 3, 4]
a = b
se eu pedir para mudar o valor da posição 2 da lista B ele acaba mexendo na lista A também... (peculiaridade do python)

Para apenas copiar sem ter essa ligação, será necessário executar o comando a seguir:
b = a[:] -> Apenas uma cópia dos valores de A

'''







#AULA 18 - LISTAS (PARTE 2) - VARIÁVEIS COMPOSTAS (LISTAS)
'''
Colocar listas dentro de listas

DECLARAÇÃO
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0]) = Pedro
print(pessoas[1][1]) = 19
print(pessoas[1])    = ['Maria', 19]



Após ter uma lista, para limpar esta basta apenas dar o comando .clear()

dado.clear() - Limpa todos os dados da lista


ex:
galera = list()
dado = list()
totmai = totmen = 0

for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
'''







#AULA 19 - DICIONÁRIOS (VARIÁVEIS COMPOSTAS)
'''
DADOS
    0        1   
'PEDRO',     25

dados = dict() ou
dados = {}
dados = {'nome':'PEDRO', 'idade':25}

print(dados['nome'])
print(dados['idade'])


Para adicionar um novo item dentro do meu dicionário
dados['sexo'] = 'M'

Para remover elementos do dicionário
del dados['idade']

filme = {'titulo':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }

print(filmes.values()) - irá retornar todos os valores do dicionário
'Star Wars', 1977, 'George Lucas'

print(filmes.keys()) - Irá retornar todas as chaves definidas
'título', 'ano', 'diretor'

print(filmes.items()) - Irá retornar todos os valores do dicionário + todas as chaves


exemplo:
for k, v in files.items():
    print(f'O {k} é {v}')

as 3 repostas que vamos ter do for de cima:
'O título é Star Wars'
'O ano é 1977'
'O diretor é George lucas'

é possível colocar os dicionários dentro de listas.

pode ser usado comandos como:
print(locadora[2]['título'])
print(locadora[0]['ano'])


PARA COLOCAR UM DICIONÁRIO DENTRO DE UMA LISTA

brasil.append(estado.copy()) - necessário usar esse método interno, não é possível usar fatiamento [:]


PARA ORDERNAR UM DICIONÁRIO
- importar a função itemgetter do módulo Operator
- gerar um novo dicionário (recomendável)
- usar a função sorted(dicionário.items(), key=itemgetter(número da coluna que contém o que quero ordenar))
'''







#AULA 20 - FUNÇÕES (PARTE 1)
'''
Função = rotina - uma coisa que você faz constantemente.

def mostralinha():
    print('-------------------------------------')



def mensagem(msg):
    print('-------------------------------------')
    print(msg)
    print('-------------------------------------')
Depois é possível digitar:
mensagem('SISTEMA DE ALUNOS') e ele vai imprimir isso na tela.



def soma(a, b):
    s = a + b
    print(s)

    
$Programa Principal
soma(4, 5)
soma(1, 3)
soma(4, 9)
soma(a=4, b=5) - Pode mudar qual argumento é qual explicitando a variável



EMPACOTAMENTO DE DADOS NAS FUNÇÕES
def contador(*num):

contador(1, 3, 5, 6, 5, 4)
vai ser criado uma tupla com todos os valores passados.



Caso necessário utilizar a função sleep sem que ela esteja bufferizando
necessário utilizar o comando 
print(num, flush=True)
'''








#AULA 21 - FUNÇÕES (PARTE 2)
'''
- INTERACTIVE HELP
help()

no terminal do python, entrar primeiro digitando:
python
help(objeto que precisa de ajuda)

ou imprimir o doc da função
print(input.__doc__)

- DOCSTRINGS
é uma string de documentação
ex:

def contador(i, f, p): adicionar o manual dentro de aspas duplas 3x logo abaixo da def da função
"""
-> Faz uma contagem e mostra na tela.
:param i: início da contagem
:param f: fim da contagem
:param p: passo da contagem
:return: sem retorno
"""

- ARGUMENTOS OPCIONAIS
definir valores para uma variavel dentro de uma função

def teste(a, b, c=0) - se o usuário não informar a variável, ela recebe 0



- ESCOPO DE VARIÁVEIS
Definição de variável global e variável local.
Para usar uma varável local como global, colocar dentro da função o comando
    global a - isso vai fazer com que o programa use a variável global dentro da função.


- RETORNO DE VALORES
Palavra mágica é return

ex:
def soma(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
'''


#AULA 22 - MÓDULOS E PACOTES
'''
MODULARIZAÇÃO:
Conforme os programas foram ficando maiores, houve a necessidade da modularização, ou seja particionar o programa todo em pequenos pedaços de códigos, conseguindo assim uma melhor visualização do código e organização.

- Sistemas ficando cada vez maiores
- Foco: Dividir um programa grande
- Foco: Aumentar a legibilidade
- Foco: Facilitar a manutenção do código

Criar um próprio módulo (biblioteca) que pode ser chamada utilizando o comando:
import "biblioteca" - Sem aspas.

VANTAGENS DA MODULARIZAÇÃO:
- Organização do código
- Facilita a manutenção do código
- Ocultação do código detalhado
- Reutilização em outros projetos



PACOTES
Definição: Uma pasta que contém módulos, caso os módulos ficarem muito grandes...

Dentro do pacote ter um arquivo de funções somente para tratamento de números, em outro somente para tratamento de strings, Funções compatíveis com datas, e outras que podem ser para tratamento de cores...

Dentro de um arquivo .py qualquer arquivo pode ser feito um módulo.
Jogando esses arquivos dentro de uma pasta, essa pasta pode ser considerada um pacote.

Posso colocar um arquivo especial dentro de cada pasta de pacote:
__init__.py

Dentro do __init__.py é onde devo de colocar todo o código relacionado aos módulos.
'''


'''
SUBSTITUIÇÃO DE CARACTERES DE UMA STRING
Caso eu querer substituir algum caractere de uma string usar o comando .replace
print(f'{valor}'.replace('.', ','))
'''



#AULA 23 - TRATAMENTO DE ERROS E EXCEÇÕES
'''
try:                    #Tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:                 #Se der falha vai executar isso.
    print(f'Problema encontrado foi {erro.__class__}')
else:                   #Se der certo, vai executar isso.
    print(f'O resultado é {r}')
finally:                #Para encerrar será executado isso, indiferente de certo ou errado
    print('Volte sempre, muito obrigado!')    


Um mesmo comando try, pode ter vários comandos excepts
try:
except TypeError:
except ValueError:
except OSError:
else:
finally:

try:
except (ValueError, TypeError)
'''