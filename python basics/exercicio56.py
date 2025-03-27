#Desafio 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media_idade = 0
mais_velho = 0
mulheres = 0
for i in range(1,5):
    print('----{}ª pessoa----'.format(i))
    nome = input('Digite o nome da {}ª pessoa: '.format(i)).strip()
    idade = int(input('Digite a idade de {}: '.format(nome)))
    media_idade += idade
    sexo = input('Digite o sexo de {} (M/F): '.format(nome)).upper()
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        pessoa = nome
    if sexo == 'F' and idade < 20:
        mulheres =+ 1
print('A média de idade do grupo é de {:.0f} anos.'.format(media_idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(mais_velho, pessoa))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
