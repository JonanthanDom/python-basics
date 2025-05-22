'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n = int(input('Digite um número: ')) 
soma = 0   
cont = 1
maior = n
menor = n
play = input('Quer continuar? (Y/N)').upper()
soma = n
while play == 'Y':
    n = int(input('Digite um número: '))   
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    play = input('Quer continuar? (Y/N)').upper()
media = soma/cont
print(f'Você digitou {cont} números e a média deles é: {media}.')
print(f'O maior número foi {maior} e o menor foi {menor}')
