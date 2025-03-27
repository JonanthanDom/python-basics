#Desafio 11:Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Qual a altura da sua parede?'))
largura = float(input('Qual a largura da sua parede?'))
area = altura*largura
tinta = area/2
print('A sua parede tem {} de altura e {} de lagura com àrea de {:.2f}m². \npara pintar essa parede você precisará de {:.1f} litros de tinta'.format(altura, largura, area, tinta))
