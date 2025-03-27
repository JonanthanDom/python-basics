#Desafio 40: Crie um programa que leia tres notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if media >= 7.0:
    print('A média foi {}, você está aprovado!'.format(media))
elif media < 5.0:
    print('Sua média foi {}, você está reprovado!'.format(media))
else:
    print('Sua média foi {}, você vai para a recuperação.'.format(media))