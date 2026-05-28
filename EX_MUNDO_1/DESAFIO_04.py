#Monte um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
#informações possíveis sobre ele.

'''
algo = input('Digite algo: ')
print('Você digitou: {}'.format(algo))
print('O tipo primitivo do que foi digitado é: ', type(algo))
print('É um número: {}'.format(algo.isnumeric()))
print('É alfabético: {}'.format(algo.isalpha()))
print('É alfanumérico: {}'.format(algo.isalnum()))
print('Está em maiúsculas: {}'.format(algo.isupper()))
print('Está em minúsculas: {}'.format(algo.islower()))
print('Está capitalizado: {}'.format(algo.istitle()))
print('Pode ser printado: {}'.format(algo.isprintable()))
print('É um espaço: {}'.format(algo.isspace()))
print('É um dígito: {}'.format(algo.isdigit()))
print('É um identificador: {}'.format(algo.isidentifier()))
print('É um decimal: {}'.format(algo.isdecimal()))
'''





#Monte um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
#informações possíveis sobre ele.
entrada_teclado = input('Digite algo para que possa ser avaliado o tipo primitivo e todas as informações disponíveis sobre ele: ')
print('O tipo primitivo da variável digitada é: {}'.format(type(entrada_teclado)))  #Identificar qual o tipo primitivo de variável
print('É numérico: {}'.format(entrada_teclado.isnumeric()))                         #identifcar se é numérico a variável
print('É alfabético: {}'.format(entrada_teclado.isalpha()))                         #Identificar se é alfabético
print('É alfanumérico: {}'.format(entrada_teclado.isalnum()))                       #Identificar se é alfanumérico
print('É minúsculo: {}'.format(entrada_teclado.islower()))                          #Identificar se é alfabético minúsculo
print('É maiscula: {}'.format(entrada_teclado.isupper()))                           #Identificar se é alfabético maiúsculo
print('É decimal: {}'.format(entrada_teclado.isdecimal()))                          #Identificar se é numérico decimal
print('É printável: {}'.format(entrada_teclado.isprintable()))                      #Identificar se pode ser printado
print('É capitalizada: {}'.format(entrada_teclado.istitle()))                       #Identificar se possui algum caractere maiúsculo
print('É um espaço: {}'.format(entrada_teclado.isspace()))                          #Identificar se é apenas um espaço 