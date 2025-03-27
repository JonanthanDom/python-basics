#Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#  de um atleta e mostre sua categoria, de acordo com a idade:
# 9 anos mirim
# 14 anos infantil
# 19 anos junior
#25 anos senior
# acima de 25 anos master
from datetime import datetime
nasc = int(input('Digite o ano do seu nascimento: '))
ano = datetime.now().year
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade >= 26:
    print('Classificação: MASTER')
elif idade >= 19:
    print('Classificação SENIOR')
elif idade >= 14:
    print('Classificação JUNIOR')
elif idade >= 9:
    print('Classificação INFALTIL')
else:
    print('CLassificação MIRIM')