def moeda(preço=0, moeda='R$'):
    res = (f'{moeda}{preço:>8.2f}'.replace('.', ','))
    return res


def aumentar(preço=0, taxa=0, format=False):
    res = preço + preço*taxa/100
    if format == True:
        moeda(res)
    return res


def diminuir(preço=0, taxa=0, format=False):
    res = preço - preço*taxa/100
    if format == True:
        moeda(res)
    return res


def dobrar(preço=0, format=False):
    res = preço*2
    if format == True:
        moeda(res)
    return res


def metade(preço=0, format=False):
    res = preço/2
    if format == True:
        moeda(res)
    return res