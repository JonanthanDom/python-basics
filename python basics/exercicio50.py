#Desafio 50: Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma  = 0
impares = []
for i in range(1 ,7):
  num = int(input('Digite um número: '))
  if num % 2 ==0:
    soma = soma + num
  elif num % 2 == 1:
    impares.append(i)
print('A soma dos números pares digitados é: {} \nOs números Impares foram {}'.format(soma, impares))