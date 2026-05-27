#Escreva um programa que leia um valor e metros
#e o exiba convertido em cm e mm
#Quilometros, Hectômetros, Decâmetros, decímetros 

valor = float(input('Escreva um valor em metros, e eu lhe respondo o mesmo valor convertido: '))
print('O valor informado é: {:.1f}m\n'.format(valor))
print('Quilometros (Km): {:.3f} \nHectômetros (Hm): {:.2f} \nDecâmetros (Dcm): {:.1f}'.format(valor/1000, valor/100, valor/10))
print('Decímetro (dm): {:.1f} \nCentímetro (cm): {:.1f} \nMilímetro (mm) é: {:.1f}'.format(valor*10, valor*100, valor*1000))
