#Crie um algoritmo que leia um número e 
#Mostre o dobro, triplo e a raiz quadrada

n = float(input('Digite um número para que possa ser calculado o dobro, triplo e raiz quadrada: '))
print('O número digitado foi {:.0f}\no dobro deste número é {:.0f}\no triplo dele é: {:.0f}\n a raiz quadrada é: {:.2f}'.format(n, 2*n, 3*n, n**(1/2)))
#{:.0f} - significa que irá ser mostrado nenhuma casa decimal do ponto flutuante no prompt
#{:.2f} - significa que irá ser mostrado apenas 2 casas decimais do número em ponto flutuante em prompt


