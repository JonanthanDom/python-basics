#Desafio 54:Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
idade = []
maior = 0
menor = 0
for i in range(1,8):
    data=int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(i)))
    idade.append(data)
for ano in idade:
    if datetime.now().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(' Ao todo temos {} pessoa maiores de idade \n e {} pessoas menores de idade'.format(maior, menor))
        