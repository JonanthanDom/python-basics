#Desafio 8:Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
d = float(input('Informe a distância em metros: '))
Km = d/1000
Hm = d/100
Dam = d/10
Dm = d*10
Cm = d*100
Mm = d*1000
print('A medida de {} em metros corresponde a: \n{}Km \n{}Hm \n{}Dam \n{:.0f}Dm \n{:.0f}cm \n{:.0f}Mm'.format(d, Km, Hm, Dam, Dm, Cm, Mm))
