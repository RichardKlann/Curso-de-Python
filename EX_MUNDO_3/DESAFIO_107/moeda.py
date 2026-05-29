def aumentar(preço, taxa):
    res = preço + preço*taxa/100
    return preço

def diminuir(preço, taxa):
    res -= preço - preço*taxa/100
    return res


def dobrar(preço):
    res = preço*2
    return res


def metade(preço):
    res = preço/2
    return res

