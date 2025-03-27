#Desafio 29: Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro?'))
if velocidade >= 81:
    multa = (velocidade - 80)*7
    print('VOCÊ EXCEDEU O LIMITE DE 80Km/h!')
    print('Deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha uma ótima viagem!')