'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um
valor lógico(opcional) indicando se será mostrado ou não na tela o processo de 
cálculo fatorial.

print(fatorial(5, show=True))
'''
#Funções
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: número inteiro a ser calculado.
    :param show: (opcional) Mostra ou não o cálculo.
    :return: O valor do fatorial de um número num.
    """

    from time import sleep
    cont = num
    calc = 1
    print('-' * 25)
    while cont > 0:
        calc *= cont
        if show == True:
            if cont == 1:
                sleep(0.5)
                print(f'{cont} = ', end='', flush=True)
                sleep(0.5)
                break
            else:
                sleep(0.5)
                print(f'{cont} x ', end='', flush=True)
        cont -= 1
    return calc
    


#Programa Principal
help(fatorial)
fatorial()
#print(fatorial(5))