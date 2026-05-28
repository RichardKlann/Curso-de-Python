'''
Crie uma tupla preenchida pelos 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time chapecoense
'''

classificacao = ('PALMEIRAS', 'FLAMENGO', 'FLUMINENSE', 'SÃO PAULO', 'ATHLETICO-PR',
                'BAHIA', 'CORITIBA', 'BOTAFOGO', 'BRAGANTINO', 'VASCO DA GAMA',
                'GRÊMIO', 'CRUZEIRO', 'EC VITÓRIA', 'CORINTHIANS', 'ATLÉTICO-MG',
                'INTERNACIONAL', 'SANTOS', 'MIRASSOL', 'REMO', 'CHAPECOENSE')

print(f'a) Os 5 primeiros colocados são: {classificacao[:5]}')
print('=' * 100)
print(f'b) Os últimos 4 colocados da tabela são: {classificacao[-4:]}')
print('=' * 100)
print(f'c) Ordem alfabética de todos os times: {sorted(classificacao)}')
print('=' * 100)
print(f'd) Chapecoense está na posição {classificacao.index("CHAPECOENSE")+1}')
print('=' * 100)