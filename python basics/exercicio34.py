#Desafio 34: Escreva um programa que pergunte o salário de um funcionário e 
# calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Reajuste salarial. \n digite o salário do funcionário: R$'))
if salario <= 1250.00:
    novo_salario = salario + (salario * 15 /100)
    print('Quem recebia R${:.2f} passa a receber R${:.2f}'.format(salario, novo_salario))
else:
    novo_salario = salario + (salario * 10/100)
    print('QUem recebia R${:.2f} passa a receber R${:.2f}'.format(salario, novo_salario))