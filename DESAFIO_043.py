'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, e calcule o IMC e mostre
o seu status, de acordo com a tabela abaixo:

- Abaixo de 18,5: Abaixo do peso
- Entre 18,5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade morbida
'''

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Seu IMC é {:.2f} e está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} e está com SOBREPESO!'.format(imc))
elif imc >=30 and imc < 40:
    print('Seu IMC é {:.2f} e está com OBESIDADE!'.format(imc))
else: 
    print('Seu IMC é {:.2f} e está com OBESIDADE MORBIDA!'.format(imc))