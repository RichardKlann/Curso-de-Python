def moeda(preço=0, moeda='R$'):
    res = (f'{moeda}{preço:>8.2f}'.replace('.', ','))
    return res


def aumentar(preço=0, taxa=0, format=False):
    res = preço + preço*taxa/100
    if format == True:
        res1 = moeda(res)
    return res1


def diminuir(preço=0, taxa=0, format=False):
    res = preço - preço*taxa/100
    if format == True:
        res1 = moeda(res)
    return res1


def dobrar(preço=0, format=False):
    res = preço*2
    if format == True:
        res1 = moeda(res)
    return res1


def metade(preço=0, format=False):
    res = preço/2
    if format == True:
        res1 = moeda(res)
    return res1


def resumo (p, taxaAum=10, taxaDim=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print('Preço analisado: R$', end='')
    print(f'{p:>8.2f}')
    print('Dobro do preço:  ', end='')
    print(dobrar(p, format=True))
    print('Metade do preço: ', end='')
    print(metade(p, format=True))
    print(f'{taxaAum}% de aumento:  ', end='')
    print(aumentar(p, taxaAum, format=True))
    print(f'{taxaDim}% de redução:  ', end='')
    print(diminuir(p, taxaDim, format=True))
    print('-' * 30)