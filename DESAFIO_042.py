'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
triangulo sera formado:

Equilátero: Todos os lados iguais
Isóceles: Dois lados iguals
Escaleno: Todos os lados diferentes
'''

seg1 = float(input('Digite o tamanho do 1° segmento: '))
seg2 = float(input('Digite o tamanho do 2° segmento: '))
seg3 = float(input('Digite o tamanho do 3° segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os tamanhos de segmentos {}, {} e {} PODEM formar um triângulo!'.format(seg1, seg2, seg3))
    if seg1 == seg2 ==seg3:
        print('E como todos os segmentos são iguais, é formado um triângulo Equilátero!')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('E como apenas dois lados são iguais, é formado um triângulo Isóceles!')
    else:
        print('Como todos os segmentos são de tamanhos diferentes, forma-se um triângulo Escaleno!')

else:
    print('Os tamanhos de segmentos {}, {} e {} NÃO PODEM formar um triângulo'.format(seg1, seg2, seg3))