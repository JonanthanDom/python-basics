#Desafio 35:Desenvolva um programa que leia o comprimento de três retas
#  e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
s1 = float(input('Digite o valor do primeiro segmento:'))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima não podem formar um triangulo.')