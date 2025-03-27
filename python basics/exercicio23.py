#Desafio 23: Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.

number = int(input('digite um número entre 0 e 9999: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print('Analisando o npumero: {}'.format(number))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'. format(c))
print('Milhar: {}'.format(m))
