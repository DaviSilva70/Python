"""Escreva um programa que pergunte o salario de un funcionario e calcule o valor do seu aumento.
Para Salario superiores a R$1.250.00, calcule um aumento de 10%.
Para Salarios Inferiores ou iguais ,o aumento e de 15%."""

salario = float(input('Digite o Salario do Colaborador R$:  '))
if salario <=1250:
     novosalario = salario + (salario * 15 /100)
else:
    novosalario = salario + (salario * 10 / 100)
print('Voçe Ganhava R$: {:.2F} agora voçe passa a ganhar  R$: {:.2F} de  Aumento'.format(salario,novosalario))
