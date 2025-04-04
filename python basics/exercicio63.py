'''Desafio 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('-'*25)
print('SEQUENCIA DE FIBONACCI')
print('-'*25)
termos = int(input('Quantos termos você quer mostrar? '))
f0 = 0
f1 = 1
fn = 2
print(f0, '>', f1, '>', end=' ')
termos -=2
while termos >0:
    fn = f0 + f1
    print(fn, '>', end=' ')
    f0 = f1 
    f1 = fn
    fn = (f0 -1) + (f1-2)
    termos -= 1
