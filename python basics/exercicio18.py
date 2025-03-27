#Desafio 18:Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, tan, sin, radians
angulo = float(input('Digite o angulo que você deseja: '))
radi = radians(angulo)
sen = sin(radi)
coss = cos(radi)
tang = tan(radi)
print('O angulo de {}, tem o seno de: {:.2f}'.format(angulo, sen))
print('O angulo de {}, tem o cosseno de: {:.2f}'.format(angulo, coss))
print('O angulo de {}, tem a tangente de: {:.2f}'.format(angulo, tang))