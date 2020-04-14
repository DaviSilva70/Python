'''Faça um programa que leia  un ano qualquer e mostre se ele e BISSEXTO.'''

from  datetime import date 
ano = int(input('Digite seu Ano e 0 para o Ano Atual : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} e Bissexto'.format(ano))
else:
    print('O Ano e {} Nao e Bissexto'.format(ano))
