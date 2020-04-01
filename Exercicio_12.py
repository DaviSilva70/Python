''' Faça um Algoritmo que leia e o preço da um produto e mostre seu novo preço .Com % de desconta. '''
produto = float(input('Qual eo Preço do Produto: R$ '))
novo = produto-(produto * 5/ 100)
print('O Valor do Produto que custava Tanto R$ {:.2f} vai custar R$ {:.2f}\n'.format(produto,novo))



preço = float(input('O Produtos Custa R$: '))
valor = preço-(preço * 5 /100)
print('Ele Custara Tanto R$:{:.2F} vai Ficar R$:{:.2F}'.format(preço,valor))
