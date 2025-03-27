#Desafio 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        tot += 1
if tot == 2:
    print('O núemro {} é primo'.format(num))
else:
    print('o número {} não é primo'.format(num))