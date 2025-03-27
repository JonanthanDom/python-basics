#Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('=-='*30)
print('Simulador de financiamento residencial ')
print('=-='*30)
valorCasa = float(input('qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário?'))
tempo = float(input('De quantos anos será o financiamento?'))*12
mensalidade = valorCasa / tempo
if mensalidade > (salario * 30/100):
    print('Para comprar uma casa de {:.0f} em {:.0f} meses, o valor da prestação será {:.2f}'.format(valorCasa, tempo, mensalidade))
    print('por isso o empréstimo não foi aprovado.')
else:
    print('Para comprar uma casa de {:.0f} em {:.0f} meses, o valor da prestação será {:.2f}'.format(valorCasa, tempo, mensalidade))
    print('Empréstimo aprovado, parabéns!!!!')