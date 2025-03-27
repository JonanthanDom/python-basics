#desafio 22: crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas e minusculas
#a quantidade de letras, sem contar os espaços
#quantas letras tem o primeiro nome

name = input('Digite seu nome: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: ', name.upper())
print('Seu nome em minúsculs é: ', name.lower())
print('Seu nome tem ao todo {} letras'. format(len(name) - name.count(' ')))
name = name.split()
print('Seu primeiro nome é: {} e ele tem {} letras.'.format(name[0], len(name[0])))