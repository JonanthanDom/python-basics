#Faça um algoritmo que leia o salário de um funcionário
#  e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário a ser reajustrado? R$'))
novo = salario + (salario * 15 / 100)
print('O salário R${:.2f} com 15% de aumento será R${:.2f}'.format(salario, novo))