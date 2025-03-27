# Desafio 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome: ').strip()
nome = nome.split()
print('Prazer em te conhecer!!!!')
print('A primeira palavra do seu nome é: {}'.format(nome[0]))
print('A ultima letra do seu nome é: {}'.format(nome[-1]))
