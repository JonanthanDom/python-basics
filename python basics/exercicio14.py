#Desafio 14:  Escreva um programa que converta uma temperatura digitando em graus Celsius 
# e converta para graus Fahrenheit.
celsius = float(input('Qual a temperatura em Celsius?'))
farenheit = (celsius * 1.8) + 32
print('A temperatura {}ºC é equivalente a {}ºF'.format(celsius, farenheit))