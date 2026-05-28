'''Crie um programa que leia quanto uma pessoa tem de dinheiro
na carteira e mostre quantos dolares ela pode comprar
U$1.00=R$3.27'''

carteira = float(input('Informe quanto de dinheiro possui na carteira: '))
print('Com o valor de R$ {:.2f} em carteira, e considerando um valor de U$1.00 = R$3.27'.format(carteira))
print('Ao trocar a moeda você terá U${:.2f}'.format(carteira/3.27))
