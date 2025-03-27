#Desafio 24: Crie um programa que leia o nome de uma cidade diga
#  se ela começa ou não com o nome “SANTO”.
name = input('Digite a cidade que você nasceu: ').strip()
name = name.upper()
name = name.split()
valor = name[0] == 'SANTO'
print(valor)