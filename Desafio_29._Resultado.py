# coding=utf-8
'''Escreva um programa que leia a velocidade de um carro . Se ele ultrapassar 80km/h,mostre
uma msg que ele foi multado. 
A multa vai custar R$ 7.00 por cada km acima do limite.'''

# Radar Eletronico.
velocidade =float(input('Sua Velocidade e de  :'))
if velocidade > 80:
    print('Voce Foi Multado Excedeu o Limite da Via 80KM/H ')
    multa = (velocidade-80) * 7.23
    print('Valor da Sua Multa e de R$: {:.2F}'.format(multa))
print('Tenha um Bom Dia Dirija com Segurança.')
