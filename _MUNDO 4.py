#PROGRAMAÇÃO EM PYTHON COM ORIENTAÇÃO A OBJETOS
'''
BIBLIOGRAFIA RECOMENDADA
- Introdução à Programação com Python - Nilo Ney Coutinho Menezes
- Object-Oriented Python - Master OOP by Building Games and GUIs - IRV KALB
- Python 3 the Comprehensive Guide - Johanes Ernest
'''

#FUNDAMENTOS
'''
DE ONDE VEM A PROGRAMAÇÃO ORIENTADA A OBJETOS?

POO - Programação Orientada a Objetos
OOP - Object Oriented Programming

"Representar elementos do mundo real nos sistemas computacionais"

"Crise do Software" de 1960?

1950 - Início das linguagens de baixo nível: assembly
1955 - Linguagens lineares - Fortran, Cobol, C, Basic
1960 - Linguagens estruturadas
1965 - Linguagens modulares
1970 - Linguagens orientadas a objetos

OOAD - Object Oriented Analysis and Design
UML - Unified Modeling Language
'''

#AULA 2 - 6 VANTAGENS DA POO
'''
C - Confiável
O - Oportuno
M - Manutenível
E - Extensível
R - Reutilizável
N - Natural
a...
d...
a...

Confiável - O isolamento entre as partes gera algo mais seguro. Ao alterar uma das partes, nenhuma outra é afetada
Oportuno - Ao dividir tudo em partes, cada uma pode ser desenvolvida em paralelo.
Manutenível - Atualizar é mais fácil. Uma pequena alteração vai beneficiar todas as partes relacionadas.
Extensível - Um sistema não deve ser estático. Tudo deve mudar e crescer para permanecer útil.
Reutilizável - Objetos que foram criados para um sistema podem ser aproveitados em outros sistemas.
Natural - Mais fácil de entender. Maior atenção às funcionalidades do que aos detalhes de implementação.
'''

#AULA 3 - CURSO PYTHON - FUNDAMENTOS O QUE SÃO OBJETOS E CLASSES?
''''
Uma forma de biscoitos. Fazem biscoitos sempre do mesmo formato, porém podem ser decorados de formas diferentes, ou até mesmo terem sabores diferentes, porém sempre tem o mesmo formato.
Essa forma, deve de ser chamada de classe! 

Classe é um formato a ser seguido sempre que eu precisar fazer objetos do mesmo tipo ou que tenham as mesmas características, ou que tenham os mesmos comportamentos.
A planta baixa de uma casa é uma classe, a forma de um biscoito, é uma classe, o projeto de desenho de um carro também é uma classe.
A forminha de biscoito, não é um objeto, não é o biscoito em si. A planta baixa ainda não é a casa, é apenas uma classe. O desenho estrutural não é um carro.

Diagrama de classes UML
- Retângulo dividido em 3 partes.

Parte de cima - NomeClasse
Caixa do meio - Características que o objeto dessa classe vai ter
Caixa de baixo - coisas que posso fazer, ou que podem ser feitos com a classe.

As características vamos chamar de ATRIBUTOS
Coisas que eu posso fazer, ou podem ser feitos serão os MÉTODOS.

Ex:
CLASSE - BiscoitoCoração
ATRIBUTOS - Tamanho, Massa, Peso, Cobertura, Cozido, Temperatura
MÉTODOS - Cozinhar(), congelar(), cobrir(), confeitar(), podeComer(), comer()

INSTÂNCIA - Início da atividade de criar o objeto.
Depois de já ter a planta baixa, a partir do momento que o pedreiro começa a construir, ele já está instanciando uma casa.
(seguir o padrão que foi definido na classe para poder criar o objeto)
"O objeto é a instância de uma classe"

Objeto = "Coisa material ou abstrata que é feito a partir de um modelo, e pode ser descrita por meio das suas características, comportamentos e estado atual."

Objeto com suas características (biscoito de coração):
tamanho = 8,2cm
massa = baunilha
peso = 54,3g
cobertura = pistache
cozido = True
temperatura = 55°C

A todas essas características, damos o nome de ESTADO!

Exemplo de objetos abstratos:
- Consulta marcada em um médico.
- Um processo de venda
- Um compromisso ou reunião
- Uma aula na faculdade
- Uma transação bancária
- Uma reserva de voo
- Um erro no sistema

Pergunta 11 - Qual dos objetos abaixo seria o único objeto abstrato da lista?
A - Sensor
B - Robô
C - Notificação
D - Livro

Letra C


Pergunta 12 - Na teoria de OO, o termo usado para o ato de fazer um objeto existir, a partir de um modelo se chama:
A - Instanciar
B - Classificar
C - Objetificar
D - Forjar

Letra A


Pergunta 13 - Todo objeto tem uma lista de atividades que podem ser feitas com ele ou que ele pode desempenhar sozinho que são:
A - Atributos
B - Métodos
C - Classes
D - Instâncias

Letra B


Pergunta 14 - Ao conjunto de todos os valores de atributos de um objeto em um determinado momento, damos o nome de:
A - Identidade
B - Instância
C - Método
D - Estado

Letra D


Pergunta 15 - Coloque nos comentários a estrutura de dois objetos: um concreto e outro abstrato.
Inclua também seus principais atributos, métodos e crie um exemplo de estado para cada um deles.
'''

#AULA 04 - FUNDAMENTOS
'''
OBJETOS SÃO VARIÁVEIS EVOLUÍDAS.

OBJETOS SÃO VARIÁVEIS QUE ALÉM DE GUARDAR DADOS, PODEM FAZER COISAS COM ESSES DADOS


#DECLARAÇÃO DA CLASSE
class MinhaClasse:
    #Atributos
    '

    '
    #Métodos
    '

    '
#Declaração dos objetos
obj = MinhaClasse()


Instanciação
Método Construtor
def __init__(self)


'''