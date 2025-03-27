#Desafio 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for i in range(1,6): 
    valor = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    peso.append(valor)
maior = max(peso)
menor = min(peso)
print('O maior peso lido foi {} e o menor foi {}'.format(maior, menor))
