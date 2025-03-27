#Desafio 33:Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)
menor  = min(n1, n2, n3)
print('O maior valor é: {}'. format(maior))
print('O menor valor é: {}'.format(menor))