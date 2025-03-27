#Desafio 37: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.

numero = int(input('Digite um número para conversão: '))
opcao = int(input('Agora escolha a base para conversão: \n [1] para codigo BINARIO \n [2] para OCTAL \n [3] para HEXADECIMAL '))
if opcao == 1:
    print('Voce selecionou a opção BINARIO:')
    binario = bin(numero)[2:]
    print(binario)
elif opcao ==2:
    print('Você selecionou a opção OCTAL:')
    octal = oct(numero)[2:]
    print(octal)
elif opcao == 3:
    print('Você selecionou a opção HEXADECIMAL:')
    hexadecimal = hex(numero)[2:].upper()
    print(hexadecimal)
else:
    print('Opção inválida!!! \nencerrando programa')