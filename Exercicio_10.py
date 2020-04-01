''' Conversao de Moedas  Considere o Valor do Dolar US1,00 = R$ 5,10  -  29/03/2020 '''
real  = float(input('Quanto voce tem em sua Carteira Hoje  R$: '))
dolar = real / 5.10
euro = real / 5.70
yen = real / 0.047
rubro = real / 0.065
peso = real / 0.0062
print('Com R${:.2F} voce pode Comprar US${:.2f} e Euro:{:.2F} e Yen:{:.2f} e Rubro: {:.2f} e Peso:{:.2f}'.format(real,dolar,euro,yen,rubro,peso))