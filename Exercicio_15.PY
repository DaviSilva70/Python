# Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado ra quantidade de dias pelo quais foi alugado,Calcule o preço a pagar sabendo que o carro custa R$:60.00 dia e KM Rodado Custa R$:0.15.

diaria = int(input('Quantos dias foi  Alugado Seu Cavalo: ' ))
km = float(input('Quantos KM voce Rodou na Viagen : '))
custo = (diaria * 95) + (km * 2.60)
print('O Total a Pagar e de R$:{:.2F}'.format(custo))