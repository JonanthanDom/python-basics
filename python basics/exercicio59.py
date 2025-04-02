'''Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
TEXTO = 'CALCULADORA'
print('=-='*20)
print(TEXTO.center(55))
print('=-='*20)
print('Digite os valores a serem calculados: ')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
menu = 0
while menu != 5:
    menu = int(input('''Escolha a operação a ser realizada:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa  '''))
    if menu ==1:
        print('Você escolheu SOMAR:')
        print('Processando...')
        sleep(2)
        soma = num1 + num2
        print('A soma entre {} e {} é: {}'.format(num1, num2, soma))
        print('='*30)
        sleep(2)
    elif menu == 2:
        print('Você escolheu MULTIPLICAR: ')
        print('Processando...')
        sleep(2)
        multiplicacao = num1 * num2
        print(' A multiplicação entre {} e {} é: {}'.format(num1, num2, multiplicacao))
        print('='*30)
        sleep(2)
    elif menu == 3:
        print('Você escolheu COMPARAR: ')
        print('Processando...')
        sleep(2)
        maior = max(num1, num2)
        print('Entre {} e {}, o maior é {}'.format(num1, num2, maior))
        print('='*30)
        sleep(2)
    elif menu == 4:
        print('Você escolheu ALTERAR:')
        print('Quais os novos valores?')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('Processando...')
        sleep(2)
        print('Atualizado!\nAgora os novos valores são: {} e {}.'.format(num1, num2))
        print('='*30)
        sleep(2)
        print('O que você deseja fazer agora?')
    elif menu == 5:
        print('finalizando... Estarei aqui quando precisar.')
        sleep(1)
    else:
        print('Opção inválida')
print('Fim do programa.')
#fim do programa
