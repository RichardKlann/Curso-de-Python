'''Faça um programa que leia a altura e a largura de uma parade
e metros. Calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²'''

altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = altura*largura
print('Os valores informados foram:\nAltura: {:.1f}m\nLargura: {:.1f}m'.format(altura, largura))
print('Considerando que 1L de tinta consegue pintar 2m² de parede, você terá que comprar {:.0f} litros\nPara pintar a área de {}m² informada'.format(area/2, area))