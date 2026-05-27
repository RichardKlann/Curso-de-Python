'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja digitado errado, peça a digitação novamente até ter um valor correto.
'''
sexo = ''
sexo = str(input('Informe M / F para Masculino ou Feminino: ')).strip()

while sexo not in 'MmFf' or sexo == '':
    print('Opção inválida!')
    sexo = str(input('Por favor, informe M / F para Masculino ou Feminino: ')).strip()

if sexo in 'Mm':
    opcao = 'Masculino'
elif sexo in 'Ff':
    opcao = 'Feminino'

print('Parabéns, você escolheu a opção de sexo {}!'.format(opcao))