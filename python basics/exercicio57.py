#Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo =''
sexo = input('Digite seu sexo (M/F): ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos, por favor, informe seu sexo (M/F): ').upper()    
print('Sexo {} registrado com sucesso!'.format(sexo))
