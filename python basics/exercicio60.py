'''Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''
print('Calculo de fatorial.')
numero = int(input("Digite um número: "))  
fatorial = 1  
contador = numero  
while contador > 1:  
    fatorial *= contador  
    contador -= 1  
print(f"O fatorial de {numero} é {fatorial}")
