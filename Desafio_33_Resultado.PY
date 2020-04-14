'''Faça um programa que leia tres numeros e mostre qual e maior e qual e menor.'''

numero1 =  int(input('Dgite o Primeiro Numero: ')) 
numero2 =  int(input('Dgite o Segundo Numero: ')) 
numero3 =  int(input('Dgite o Terceiro Numero: ')) 
# Verificando quem e menor 
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
 # Verficando quem Maior Valor .   
maior = numero1
if numero2 > numero1 and numero2 < numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print('O Menor Valor Digitado {}'.format(menor))   
print('O Maior valor Digitado {}'.format(maior)) 


# Outro Exemplo. 
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor:'))

# Verificando quem e menor 
menor = a 
if b<a and b<c:
    menor = b  
if c<a and c<b:
    menor = c
# Verficando quem Maior Valor .     
maior = a  
if b>a and b>c:
     maior = b  
if c>a and c>b:
     maior = c    
print('O Menor Valor Digitado foi {}'.format(menor))
print('O Maoir Numero Digita foi {}'.format(maior)) 