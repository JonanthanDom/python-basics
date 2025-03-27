#Desafio 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.
preco = float(input('Qual o valor do produto: R$'))
desconto = preco - (preco / 20)
#outra fomra de fazer o calculo é:
#desconto = preço - (preco*5/100)
print('O valor com desconto de 5% é R${:.2f}'.format(desconto))
