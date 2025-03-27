#Desafio 38: Escreva um programa que leia dois números inteiros e compare-os.
#  mostrando na tela uma mensagem:
# O primeiro valor é maior, o segundo valor é maior ou os dois valores são iguais

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior')
elif n2 > n1:
    print('O segundo número é maior')
else:
    print('os dois números são iguais')