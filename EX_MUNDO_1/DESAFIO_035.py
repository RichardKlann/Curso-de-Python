'''
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

a + b > c
a + c > b
c + b > a

'''

seg1 = float(input('Digite o tamanho do 1° segmento: '))
seg2 = float(input('Digite o tamanho do 2° segmento: '))
seg3 = float(input('Digite o tamanho do 3° segmento: '))

''' - JEITO DIFÍCIL QUE EU FIZ...
if (seg1 + seg2) > seg3:
    if (seg1 + seg3) > seg2:
        if (seg2 + seg3) > seg1:
            print('Os tamanhos de segmentos {}, {} e {} podem formar um triângulo!'.format(seg1, seg2, seg3))
        else:
            print('Os tamanhos dos segmentos {}, {} e {} não podem formar um triângulo!'.format(seg1, seg2, seg3))
'''

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os tamanhos de segmentos {}, {} e {} PODEM formar um triângulo!'.format(seg1, seg2, seg3))
else:
    print('Os tamanhos de segmentos {}, {} e {} NÃO PODEM formar um triângulo'.format(seg1, seg2, seg3))