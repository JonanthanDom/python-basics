'''Desafio 44:  Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''

print('='*20, 'CAIXA', '='*20)
compras = float(input('Digite o valor total das compras: R$'))
forma_pgto = int(input('''              FORMAS DE PAGAMENTO
            [ 1 ] À VISTA EM DINHEIRO
            [ 2 ] DÉBITO / CRÉDITO À VISTA
            [ 3 ] PARCELADO \n'''))
if forma_pgto == 1:
    print('Pagamento à vista em dinheiro.')
    compras = compras - (compras *10 /100)
    print('O total a pagar será R${:.2f} com desconto de 10%'.format(compras))
elif forma_pgto == 2:
    print('Pagamento à vista no cartão débito / crédito.')
    compras = compras - (compras * 5 / 100)
    print('O total a pagar será R${:.2f} com desconto de 5%'.format(compras))
elif forma_pgto == 3:
    print('Pagamento parcelado.')
    parcelas = int(input('Qual a quantidade de parcelas? '))
    if parcelas <= 2:
        print('''Você vai pagar {}x de {:.2f},
              total R${:.2f} sem descontos'''.format(parcelas, (compras / parcelas), compras))
    elif parcelas > 2:
        juros = compras + (compras *20 / 100)
        print('''Você vai pagar {}x de {:.2f} com juros de 20%.
              Sua compra de R${:.2f} vai custar R${:.2f}.'''.format(parcelas, (juros/ parcelas), compras,  juros))
