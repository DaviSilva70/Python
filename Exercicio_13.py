 # Faça um Algoritmo que leia o Salrio de um funcionario e mostre seu novo Salrio ,com 15% de aumento

salario = float(input('Qual o Salrio do Funcionario? R$: '))
aumento = salario+( salario * 15/ 100)
print('Um Funcionario que Ganha R$:{:.2F},com 15% de Aumento, passa a Receber\nR$:{:.2F}'.format(salario,aumento))


# Exercicio Teste 

tv = float(input('TV em Promaçao com 10% de desconto a vista R$:'))
novo = tv-(tv * 10/100)
 # desconto = tv-(tv * 8 /100) 
print('Sua TV Smart 45P saiu de R$:{:.2F} foi para R$:{:.2f} '.format(tv,novo))


