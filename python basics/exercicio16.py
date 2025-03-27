#Desafio 16: Crie um programa que leia um número Real qualquer pelo teclado ,
# e mostre na tela a sua porção Inteira.

from math import floor
num = float(input('Digite um núemro qualquer: '))
print('O número digitado foi {}, sua porção inteira é: {}'.format(num, floor(num)))
