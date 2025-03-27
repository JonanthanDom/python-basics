# Desafio 17: Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
catoposto = float(input('digite o comprimento do cateto oposto: '))
catadjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catoposto, catadjacente)
print('A hipotenusa mede: {:.2f}'.format(hipotenusa))