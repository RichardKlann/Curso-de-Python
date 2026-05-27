'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: Reprovado!
- Média entre 5.0 e 6.9: Recuperação!
- Média 7.0 ou superior: Aprovado!
'''

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('Você possui uma média de {:.1f}. Para não estar automaticamente reprovado precisa de ao menos 5.0!'.format(media))
elif media >= 5 and media < 7:
    print('Você possuia uma média de {:.1f}. Você está em recuperação. Precisa tirar uma média maior que 7.0 para ser aprovado'.format(media))
else:
    print('Você posui uma média de {:.1f}. Parabéns, você está APROVADO!'.format(media))