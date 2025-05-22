'''Desafio 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
cont = 0
num = 0
n = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    num += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma deles foi: {}'.format(cont, num))
