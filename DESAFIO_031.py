'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km, para viagens de até 200Km e R$0,45 para viagens mais longas
'''

distancia = float(input('Informe a distância em Km da sua viagem: '))

valorKm = 0.50 if distancia <= 200 else 0.45

'''
if distancia <= 200:
    valorKm = 0.50

else:
    valorKm = 0.45'''

print('A sua viagem possui um custo por Km de R${:.2f}.'.format(valorKm))
print('Considerando que você vai percorrer {:.0f}Km, o custo total da viagem será R${:.2f}.'.format(distancia, distancia*valorKm))

