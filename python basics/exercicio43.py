'''Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / altura**2
if imc < 18.5:
    print('Seu imc é {:.2f}, \n você está abaixo do peso ideal'. format(imc))
elif 18.5 <= imc < 25.0:
    print('Seu imc é {:.2f}, \nvocê está no peso ideal.'.format(imc))
elif 25.0<= imc < 30:
    print('Seu imc é {:.2f}, \nvocê está em sobrepeso.'.format(imc))
elif 30<= imc < 40.0:
    print('Seu imc é {:.2f}, \nvocê está obeso.'.format(imc))
else:
    print('Seu imc é {:.2f}, \nvocê está com obesidade mórbida!!!'.format(imc))
