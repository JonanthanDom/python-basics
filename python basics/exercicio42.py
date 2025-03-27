#Desafio 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
# triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
s1 = float(input('Digite o valor do primeiro segmento:'))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 == s2 == s3:
    print('o triangulo formado será do tipo EQUILÁTERO.')
elif s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 == s2 or s1 == s3 or s2 == s3:
    print('O triangulo formado será do tipo ESCALENO')
elif s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 != s2 != s3:
    print('O trinagulo formado será do tipo ISÓSCELES')
else:
    print('OS segmentos acima não podem fomrar um triangulo.')
  