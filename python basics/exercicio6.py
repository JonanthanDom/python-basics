#Desafio 6:Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número:'))
d = n*2
t = n*3
r = n**0.5
print('o dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'. format(n, t))
print('A raz quadrada de {} vale {:.2f}.'. format(n, r))