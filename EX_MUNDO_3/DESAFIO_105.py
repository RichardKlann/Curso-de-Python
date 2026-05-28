'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e retornar 
um dicionário com as seguintes informações: 

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
'''

def notas(*num, sit=False):
    """
    -> Identifica a quantidade de notas, maior nota, menor nota, calcula a média.
    :param *num: adicionar todas as notas a serem calculadas.
    :param sit: Parâmetro opcional que informa qual a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    
    #quantidade de notas
    dicionario['total'] = len(num)

    #Maior número da tupla
    dicionario['maior'] = max(num)
    '''for i, v in enumerate(num):
        if i == 0:
            maior = v
        elif v > maior:
            maior = v
    dicionario['maior'] = maior'''

    #Menor número da tupla
    dicionario['menor'] = min(num)
    '''for i, v in enumerate(num):
        if i == 0:
            menor = v
        elif v < menor:
            menor = v
    dicionario['menor'] = menor'''


    #Media da tupla:
    dicionario['media'] = sum(num)/len(num)
    '''soma = sum(num)
    media = soma/len(num)
    dicionario['media'] = media'''

    #Situação da média
    if sit:
        if dicionario['media'] < 6:
            situacao = 'RUIM'
        elif 6 <= dicionario['media'] < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        dicionario['situação'] = situacao
    print('-' * 30)
    return dicionario





#Programa principal
resp = notas(10, 5, 7, 8.5, 9, sit=True)
print(resp)