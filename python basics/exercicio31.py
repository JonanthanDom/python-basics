#Desafio 31:  Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longa
from time import sleep
print('-=-'*20)
distancia = int(input('Qual a distância da sua viagem? '))
print('-=-'*20)
print('você está prestes a iniciar uma viagem de: {} km, só um minuto enquanto calculamos a sua passagem.' .format(distancia))
sleep(3)
if distancia <= 200:
    preco  = distancia * 0.50
    print('Sua passagem custa: {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Sua passagem custa {:.2f}'.format(preco))